from flask import Flask
from flask_restful import Api, Resource
from config import *
import src.routes


if __name__ == '__main__':
    app.run(port=PORT, host=HOST)
