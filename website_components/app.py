from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/website_cover.html')
def hello(name=None):
    return render_template('website_cover.html', name=name)


@app.route('/McDonalds/')
@app.route('/map/website_page_mcdonalds.html/')
def map_McDonalds(name=None):
    return render_template('website_page_mcdonalds.html', name=name)

@app.route('/Wendys/')
@app.route('/map_wendys/website_page_wendys.html/')
def map_Wendys(name=None):
    return render_template('website_page_wendys.html', name=name)

@app.route('/KFC/')
@app.route('/map/website_page_kfc.html/')
def map_KFC(name=None):
    return render_template('website_page_kfc.html', name=name)

@app.route('/Arbys/')
@app.route('/map/website_page_arbys.html/')
def map_KFC(name=None):
    return render_template('website_page_arbys.html', name=name)

@app.route('/Burger-King/')
@app.route('/map/website_page_burgerking.html/')
def map_KFC(name=None):
    return render_template('website_page_burgerking.html', name=name)

@app.route('/In-N-Out/')
@app.route('/map/website_page_in-Nout.html/')
def map_KFC(name=None):
    return render_template('website_page_in-Nout.html', name=name)

@app.route('/Chuck-E-Cheese/')
@app.route('/map/website_page_chuck.html/')
def map_KFC(name=None):
    return render_template('website_page_chuck.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)