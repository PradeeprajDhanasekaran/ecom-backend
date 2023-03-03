from server import api
from src.api.user import UserRegister
api.add_resource(UserRegister, '/')
