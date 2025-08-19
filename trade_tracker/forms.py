from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class TradeForm(FlaskForm):
    symbol = StringField("Symbol", validators=[DataRequired()])
    direction = SelectField("Direction", choices=[("LONG","LONG"),("SHORT","SHORT")], validators=[DataRequired()])
    entry_price = FloatField("Entry Price", validators=[DataRequired()])
    qty = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=1)])
    exit_price = FloatField("Exit Price", validators=[Optional()])
    screenshot = FileField("Screenshot", validators=[Optional()])
    submit = SubmitField("Save")
