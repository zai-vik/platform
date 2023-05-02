from flask_restful import Resource, reqparse
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
     email = data['email']
     
     return db.check_new_user(login, email)
