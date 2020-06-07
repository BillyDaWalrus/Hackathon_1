from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('website_cover.html', name=name)

@app.route('/McDonalds/')
def map_McDonalds(name=None):
    return render_template('website_page_mcdonalds.html', name=name)

@app.route('/Wendys/')
def map_Wendys(name=None):
    return render_template('website_page_wendys.html', name=name)

@app.route('/KFC/')
def map_KFC(name=None):
    return render_template('website_page_kfc.html', name=name)

@app.route('/Arbys/')
def map_Arbys(name=None):
    return render_template('website_page_arbys.html', name=name)

@app.route('/Burger-King/')
def map_BurgerKing(name=None):
    return render_template('website_page_burgerking.html', name=name)

@app.route('/In-N-Out/')
def map_InNOut(name=None):
    return render_template('website_page_in-Nout.html', name=name)

@app.route('/Chuck-E-Cheese/')
def map_Chuck(name=None):
    return render_template('website_page_chuck.html', name=name)
