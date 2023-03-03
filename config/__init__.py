
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os





load_dotenv()
app = Flask(__name__)
api = Api(app)

DB_CONNECTION= os.getenv('DB_CONNECTION')
DB_HOST= os.getenv('DB_HOST')
DB_PORT= os.getenv('DB_PORT')
DB_DATABASE= os.getenv('DB_DATABASE')
DB_USERNAME= os.getenv('DB_USERNAME')
DB_PASSWORD= os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI']= DB_CONNECTION +'://'+ DB_USERNAME +':'+ DB_PASSWORD +'@'+ DB_HOST + ':'+ DB_PORT+'/'+ DB_DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


HOST= os.getenv('HOST')
PORT= os.getenv('PORT')

db = SQLAlchemy(app)
app.app_context().push()

migrate = Migrate(app,db)