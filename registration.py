from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return {"login": "Some info", "password": 'wswe'}


api.add_resource(Main, '/api/login')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081, host="127.0.0.1")
