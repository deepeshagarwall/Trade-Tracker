import os
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from werkzeug.utils import secure_filename
from .. import db
from ..models import Trade
from ..forms import TradeForm

trades_bp = Blueprint("trades", __name__)

@trades_bp.route("/")
def list_trades():
    status = request.args.get("status", "ALL")
    query = Trade.query
    if status != "ALL":
        query = query.filter_by(status=status)
    trades = query.order_by(Trade.opened_at.desc()).all()
    return render_template("trades.html", trades=trades, status=status)

@trades_bp.route("/new", methods=["GET", "POST"])
def new_trade():
    form = TradeForm()
    if form.validate_on_submit():
        filename = None
        if form.screenshot.data:
            filename = secure_filename(form.screenshot.data.filename)
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
            form.screenshot.data.save(filepath)

        trade = Trade(
            symbol=form.symbol.data.upper(),
            direction=form.direction.data,
            entry_price=form.entry_price.data,
            qty=form.qty.data,
            exit_price=form.exit_price.data if form.exit_price.data else None,
            screenshot=filename,
        )
        if form.exit_price.data:
            trade.status = "CLOSED"
            trade.closed_at = datetime.utcnow()

        db.session.add(trade)
        db.session.commit()
        flash("Trade added successfully!", "success")
        return redirect(url_for("trades.list_trades"))
    return render_template("trade_form.html", form=form)

@trades_bp.route("/<int:trade_id>")
def trade_detail(trade_id):
    trade = Trade.query.get_or_404(trade_id)
    return render_template("trade_detail.html", trade=trade)

@trades_bp.route("/<int:trade_id>/delete", methods=["POST"])
def delete_trade(trade_id):
    trade = Trade.query.get_or_404(trade_id)
    db.session.delete(trade)
    db.session.commit()
    flash("Trade deleted successfully.", "info")
    return redirect(url_for("trades.list_trades"))
