from flask_restful import Api, Resource, reqparse
from auth_db import Database
from random import randint

db = Database()

parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("email", type=str)

def send_email(email, num):
   print(f'Send code {num} for {email}')

class Reg(Resource):
   def post(self):
     data = parser.parse_args()
     print(data)
     
     login = data['login']
     password = data['password']
     email = data['email']
     code = randint(100000, 1000000)
     
     res = db.insert_temp_user(login, password, email, code)

     if res['success'] == 1:
        send_email(email, code)

     return res


