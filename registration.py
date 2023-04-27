from flask import Flask
from flask_restful import Api, Resource, reqparse
from database import Database

app = Flask(__name__)
api = Api()

db = Database()

parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("email", type=str)

class Main(Resource):
    def post(self):
      data = parser.parse_args()

      login = data['login']
      password = data['password']
      email = data['email']

      db.insert_user(login, password, email)

      return


api.add_resource(Main, '/api/reg')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081, host="127.0.0.1")
