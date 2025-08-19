# Trade Tracker (Refactored)

A Flask app to track trades with Bootstrap 5 UI and Chart.js dashboard.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
flask db init
flask db migrate -m "init"
flask db upgrade
flask run
```
