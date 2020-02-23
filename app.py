from flask import Flask
from flask_pymongo import PyMongo
import logging
from flask_cors import CORS

app = Flask('sms-analytics')
app.secret_key = "gp73LzuvRM"

if app.config["ENV"] == "production":
  app.config["MONGO_URI"] = ENV['MONGODB_URI']
  logging.basicConfig(filename='log/production.log',level=logging.INFO)
else:
  logging.basicConfig(filename='log/development.log',level=logging.DEBUG)
  app.config["MONGO_URI"] = "mongodb://localhost:27017/sms_analytics"

# logging.debug("---ENV--------APP-{}---".format(app.config["ENV"]))

mongo = PyMongo(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})