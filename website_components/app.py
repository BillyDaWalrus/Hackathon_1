from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/website_cover.html')
def hello(name=None):
    return render_template('website_cover.html', name=name)


@app.route('/map_McDonalds/')
@app.route('/map/website_map_page.html/')
def map_McDonalds(name=None):
    return render_template('website_map_page.html', name=name)

@app.route('/map_wendys/')
@app.route('/map_wendys/webiste_map_wendys.html/')
def map_Wendys(name=None):
    return render_template('webiste_map_wendys.html', name=name)

@app.route('/map_kfc/')
@app.route('/map/webiste_page_kfc.html/')
def map_KFC(name=None):
    return render_template('webiste_page_kfc.html', name=name)