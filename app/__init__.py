from flask import Flask, render_template, request, send_from_directory
import jinja2
import smtplib
import os
from flask_cors import CORS
# Configure application
app = Flask(__name__, template_folder='templates')
CORS(app)
app.static_folder = 'static'
# app.template_folder='templates'
# subscribers = []  


myloader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader(['templates']),])
app.jinja_loader = myloader

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')  


@app.route('/portfolio')
def portfolio():
    title = 'Portfolio - Khalid Gharib'
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    title = 'Blog - Khalid Gharib'
    return render_template('blog.html')

@app.route('/about')
def about():
    title = 'About Me'
    return render_template('about.html')

@app.route('/contact')
def contact():
    title = 'Contact Info - Khalid Gharib'
    return render_template('contact.html')

@app.route('/subscribe')
def subscribe():
    title = 'Subscribe - Khalid Gharib'
    return render_template('subscribe.html')