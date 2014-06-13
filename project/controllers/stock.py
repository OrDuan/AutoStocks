from flask import render_template
from project import app
from project.models.db_helper import save
from project.models.stock import Stock


@app.route('/stockinfo')
def stock_info():
    """
    Page that shows all the submitted orders with an option to confirm it
    """
    stocks = Stock.query.filter_by().all()
    return render_template('stock_info.html', stocks=stocks)

@app.route('/')
def index():
    return "home"