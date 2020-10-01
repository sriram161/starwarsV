from flask import Flask
from flask-restplus import Api, Resource
from application.server import app

api = Api(app, version='1.0', title='Starwars films.',
          description='get all the starwars films.')

film_namespace = api.namespace('films', description='starwar film information')


class Films(Resource):
    '''This api have a post service to get all films form starwars'''

    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201
