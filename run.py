from app import app, mongo, logging
import json, logging
from bson.json_util import dumps
from flask import jsonify, request
from flask import render_template
from datetime import datetime, timedelta
import pymongo #----Added for sorting stuff


OTPLIST_TABLE = mongo.db.otplist

@app.route('/api')
def index():
  return "Api working"

@app.route('/')
def otplist():
  today = datetime.today()
  otplist = OTPLIST_TABLE.find(sort=[( 'created_at', pymongo.DESCENDING )] ).limit(5)
  return render_template("otplist.html", otplist = otplist)

@app.route('/api/add_otp', methods=['POST'])
def addotp():
  # import pdb; pdb.set_trace()
  try:
    if 'otp_token' not in request.json:
      return jsonify({'message': 'Error in params'})
    else:   
      otp_token = request.json['otp_token']
      id = OTPLIST_TABLE.insert({'otp_token': otp_token, "created_at": datetime.now()})

      resp = jsonify({'message':'Token added successfully!'})
      resp.status_code = 200
      return resp
  except Exception as e:
    logging.debug("-------EXCEPTION---{}---".format(e.args))
    return jsonify({'message': "Exception occured ".format(e.args) })
  # else:
  #   return not_found()

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found"


if __name__ == "__main__":
    app.run(debug=True)