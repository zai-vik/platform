from flask_restful import Api, Resource, reqparse
from auth_db import Database

db = Database()

parser = reqparse.RequestParser()
parser.add_argument("code", type=str)

class CheckUp(Resource):
    def post(self):
        data = parser.parse_args()

        code = data['code']

        return db.check_code(code)


# platorm.email.validation@gmail.com
# QWER2006ZXCV