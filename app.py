from flask import Flask
import mysql.connector
import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api  = Api(app)

