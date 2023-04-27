from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return {"login": "Some info", "password": 56}


<<<<<<< HEAD
api.add_resource(Main, "/api/login")
=======
api.add_resource(Main, '/registration.py')
>>>>>>> d5c2076ec7389943f5de3836cba9419cdb2d52fe
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081, host="127.0.0.1")
