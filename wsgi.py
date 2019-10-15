from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
	return "<p> Sucessfully Deployed Python Flask Web Application to OpenShift Cloud (Container Application Platform by Red Hat!) <br/><br/> <a href='/about'> About Page </a> </p>"

@application.route('/about')
def about():
	return "<p> Hi there, I am Akash, You can Call Me AkashJeez, I Love Coding and Racing :) <br/><br/> <a href='/'> Index Page </a> </p>"

if __name__ == '__main__':
	application.run(debug = True)
