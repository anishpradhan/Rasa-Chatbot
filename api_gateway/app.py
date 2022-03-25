from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)


api.add_resource(CustomActionAPI, '/custom_actions', endpoint='custom_actions')
api.add_resource(Conversations, '/conversation/<conversation_id>', endpoint='conversation')
