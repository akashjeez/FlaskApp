from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
	return "<h2> Deployed Flask Application to OpenShift! </h2>"

if __name__ == '__main__':
	app.run(debug = True)
