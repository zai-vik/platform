from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from login import Login
from registration import Reg
from email_check import CheckUp

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
api = Api()

api.add_resource(Login, '/api/login')
api.add_resource(Reg, '/api/reg')
api.add_resource(CheckUp, '/api/checkup')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081, host="127.0.0.1")
