from flask_restful import Api, Resource, reqparse
from auth_db import Database

db = Database()

parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        print(data)

        login = data['login']
        password = data['password']

        return db.check_info(login, password)
