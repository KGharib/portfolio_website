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

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('templates/index.html')  


@app.route('/portfolio')
def portfolio():
    title = 'Portfolio - Khalid Gharib'
    return render_template('templates/portfolio.html')

@app.route('/blog')
def blog():
    title = 'Blog - Khalid Gharib'
    return render_template('templates/blog.html')

@app.route('/about')
def about():
    title = 'About Me'
    return render_template('templates/about.html')

@app.route('/contact')
def contact():
    title = 'Contact Info - Khalid Gharib'
    return render_template('templates/contact.html')

@app.route('/subscribe')
def subscribe():
    title = 'Subscribe - Khalid Gharib'
    return render_template('templates/subscribe.html')

# @app.route('/form', methods=['POST'])
# def form():
#     title = 'Form'
#     first_name= request.form.get("first_name")
#     last_name= request.form.get("last_name")
#     email = request.form.get("email")
#     # message = 'You have subscribed to my Email newsletter'

#     # server = smtplib.SMTP("smtp.gmail.com", 587)
#     # server.starttls()
#     # server.login("khalid.gharib1994@gmail.com", os.getenv("PASSWORD"))
#     # server.sendmail("khalid.gharib1994@gmail.com", email, message)

#     if not first_name or not last_name or not email:
#         error_statement = 'Missing Fields, please try again.'
#         return render_template('subscribe.html', error_statement=error_statement
#                                 ,first_name=first_name
#                                 ,last_name=last_name
#                                 ,email=email)
#     subscribers.append(f'{first_name} {last_name} | {email}')
#     return render_template('form.html',subscribers=subscribers)

