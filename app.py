from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

"""
The API takes 1 param, a boolean value of have you graduated
Returns success message of yes/no
"""

# @app.route('/')
@cross_origin()
def hello_world():
    return {"Value" : "This is my first API"}

@app.route('/post_education', methods=['GET'])
@cross_origin()
def post_education():
	graduated = 0;
	args = request.args;
	admin_message = f" These are the request parameters {args} \n"
	if('graduated' in args.keys()):
		graduated = args['graduated']
		if(graduated == "1"):
			admin_message += " You have graduated , admission success :)"
		else:
			admin_message += " You have not graduated , admission fail :("
	else:
		admin_message += " Wrong parameters sent , check again !!"
	return {"admin_message" : admin_message}
