from flask_restful import Resource
from src.models.user_model import User, db
from flask import request, jsonify, make_response


class UserRegister(Resource):
    
    def get(self):
        return 'App is running ...'

    def post(self):

        data = request.json
        existing_email = User.query.filter_by(email=data['email']).first()

        if not existing_email:

            newuser = User(first_name=data['first_name'],
                           last_name=data['last_name'],
                           mobile=data['mobile'],
                           email=data['email'],
                           password=data['password'])
            db.session.add(newuser)
            db.session.commit()
            response = {
                'message': 'User created successfully'
            }
            return make_response(jsonify(response), 201)
        else:

            respose1 = {
                'message': 'User already exist'
            }

            return make_response(jsonify(respose1), 409)
