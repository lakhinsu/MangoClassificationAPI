from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import pickle


app = Flask(__name__)

api = Api(app)

class Hello(Resource):
    def get(self):
        data = request.args
        print(data.to_dict())
        return jsonify({"message":"Hello World"})

    def post(self):
        data = request.args
        print(data.to_dict())
        return jsonify({"data":data})

api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)