"""
Test implementation of a Restful API
"""
from flask import Flask, make_response
from flask_restful import Api, Resource

CFG_PORT = 5001
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

        data = {"data": "Hi Programming Project 2024! TEST"}

        return data

class NewEndpoint(Resource):
    def get(self):
        # Creating an HTML response using make_response
        html_content = """
                <html>
                    <head>
                        <title>Felix's Page</title>
                    </head>
                    <body>
                        <h1>Hier ist Felix Endpoint</h1>
                        <h2>Welcome to Felix's custom endpoint!</h2>
                    </body>
                </html>
                """
        # Make a response object and set the content type to 'text/html'
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html'
        return response




api.add_resource(HelloWorld,'/hello')
api.add_resource(NewEndpoint,'/felix')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=CFG_PORT)
