from flask import Blueprint, render_template
from ..models import Trade

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    trades = Trade.query.order_by(Trade.opened_at.desc()).limit(5).all()
    return render_template("index.html", trades=trades)
