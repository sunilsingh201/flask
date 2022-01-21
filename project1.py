from ast import Delete
from distutils.log import debug
from importlib.resources import Resource
from unittest import result
from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



# This is the function
def checked_posted_data(posted_data,function_name):
    if (function_name == "add" or function_name == "subtract" or function_name =="multiply"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200
    elif (function_name =="divide"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 200
         

class add(Resource):
    def post(self):

        # step 01 : Get the posted data from postman
        posted_data = request.get_json()

        # step 02 : Check Whether the posted data is valid or invlaid
        # This function will verify the validity of a posted data

        status_code = checked_posted_data(posted_data,"add")
        if (status_code != 200):
            result = {
                "Message":"An error occured",
                "status code":status_code
            }
            return jsonify(result)

        x = posted_data["x"]
        y = posted_data["y"]
        x=int(x)
        y=int(y)
        output =  x+y
        result = {
            "sum":output,
            "status code":200
            
        }
        return jsonify(result)




class subtract(Resource):
    def post(self):

        # step 01 : Get the posted data from postman
        posted_data = request.get_json()

        # step 02 : Check Whether the posted data is valid or invlaid
        # This function will verify the validity of a posted data

        status_code = checked_posted_data(posted_data,"subtract")
        if (status_code != 200):
            result = {
                "Message":"An error occured",
                "status code":status_code
            }
            return jsonify(result)

        x = posted_data["x"]
        y = posted_data["y"]
        x=int(x)
        y=int(y)
        output =  x-y
        result = {
            "sum":output,
            "status code":200
            
        }
        return jsonify(result)

class multiply(Resource):
    def post(self):

        # step 01 : Get the posted data from postman
        posted_data = request.get_json()

        # step 02 : Check Whether the posted data is valid or invlaid
        # This function will verify the validity of a posted data

        status_code = checked_posted_data(posted_data,"multiply")
        if (status_code != 200):
            result = {
                "Message":"An error occured",
                "status code":status_code
            }
            return jsonify(result)

        x = posted_data["x"]
        y = posted_data["y"]
        x=int(x)
        y=int(y)
        output =  x*y
        result = {
            "sum":output,
            "status code":200
            
        }
        return jsonify(result)

class divide(Resource):
    def post(self):

        # step 01 : Get the posted data from postman
        posted_data = request.get_json()

        # step 02 : Check Whether the posted data is valid or invlaid
        # This function will verify the validity of a posted data

        status_code = checked_posted_data(posted_data,"divide")
        if (status_code != 200):
            result = {
                "Message":"An error occured",
                "status code":status_code
            }
            return jsonify(result)

        x = posted_data["x"]
        y = posted_data["y"]
        x=int(x)
        y=int(y)
        output =  (x*1.0)/y
        result = {
            "sum":output,
            "status code":200
            
        }
        return jsonify(result)


api.add_resource(add, "/add")
api.add_resource(subtract, "/subtract")
api.add_resource(multiply, "/multiply")
api.add_resource(divide, "/divide")

@app.route('/')
def hello():
    return "Hello This is successfull"

if __name__ == "__main__":
    app.run(debug=True)