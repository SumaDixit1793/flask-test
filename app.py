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
	
	#Criteria for admissions, 
	#Min years of education >= 4 years, (hence |start_year_1 - end_year_1|  + |start_year_2 - end_year_2| >= 4)
	#Atleast 1 graduation = true
	total_years_education = 0
	graduated = False
	for arg in args.keys():
		obj_found = json.loads(args[arg]);
		s_y = obj_found["start_year"].split("T")
		e_y = obj_found["end_year"].split("T")
		if(s_y):
			s_y = int(s_y[0].split("-")[0])
		if(e_y):
			e_y = int(e_y[0].split("-")[0])
		total_years_education += abs(s_y - e_y)
		graduated = obj_found["graduated"]
	if(total_years_education >= 4 and graduated):
		admin_message += f" Admission success !!! Criteria considered Years of education {total_years_education} AND graduated {graduated}"
	else:
		admin_message += f" Admission failed !!! Criteria considered Years of education {total_years_education} AND graduated {graduated}"
	return {"admin_message" : admin_message}
	
