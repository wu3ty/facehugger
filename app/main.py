"""
Test implementation of a Restful API
"""
from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime

CFG_PORT = 5000
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    """
    Test API Endpoint
    """
    def get(self):
        """
        Getter for hello world
        """
        current_time = datetime.now().time()

        if current_time.second % 2 == 0: 
            data = {"data": "Why did the programmer quit his job? Because he didn't get arrays."}
        else:
            data = {"data": "Hi Programming Project 2023!"}
        
        return data

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=CFG_PORT)
