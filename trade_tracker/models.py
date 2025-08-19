from datetime import datetime
from . import db

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), nullable=False)
    direction = db.Column(db.String(10), nullable=False)  # LONG/SHORT
    entry_price = db.Column(db.Float, nullable=False)
    exit_price = db.Column(db.Float)
    qty = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(10), default="ACTIVE")  # ACTIVE / CLOSED
    opened_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime)
    screenshot = db.Column(db.String(120))  # file path

    def pnl(self):
        if not self.exit_price:
            return None
        mult = 1 if self.direction == "LONG" else -1
        return (self.exit_price - self.entry_price) * self.qty * mult
