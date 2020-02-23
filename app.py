from flask import Flask
from flask_pymongo import PyMongo
import logging
from flask_cors import CORS

app = Flask('sms-analytics')
app.secret_key = "gp73LzuvRM"

if app.config["ENV"] == "production":
  app.config["MONGO_URI"] = 'mongodb://heroku_v20fnn1p:eelp5v7uqn2v0gl6e5d4uvcf9u@ds217548.mlab.com:17548/heroku_v20fnn1p?retryWrites=false'
  logging.basicConfig(filename='log/production.log',level=logging.DEBUG)
else:
  logging.basicConfig(filename='log/development.log',level=logging.DEBUG)
  app.config["MONGO_URI"] = "mongodb://localhost:27017/sms_analytics"

# logging.debug("---ENV--------APP-{}---".format(app.config["ENV"]))

mongo = PyMongo(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})