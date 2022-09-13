"""
Test implementation of a Restful API
"""
import os
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api =   Api(app)

@app.route('/nichtDieProvinzial')
def nichtDieProvinzial():
    programmierpojektnote = request.args.get('programmierpojektnote')

    return '''<div>{}</div>'''.format(programmierpojektnote)


class HelloWorld(Resource):
    """
    Test API Endpoint
    """
    def get(self):
        """
        Getter for hello world
        """

        data={"data": "Hi there, Programming Project!"}

        return data

api.add_resource(HelloWorld,'/hello')


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")


    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
    #Test
