from time import sleep
from flask import Flask, jsonify
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


class Hello(Resource):

    @staticmethod
    def get():
        return jsonify({'message': 'It is a sleep program'})


# another resource to respond after a number of seconds
class Sleep(Resource):

    @staticmethod
    def get(num):
        sleep(num)
        return jsonify({'sleepTime': num})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Sleep, '/sleep/<int:num>')

# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
