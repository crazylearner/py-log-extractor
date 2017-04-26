#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort

app = Flask(__name__)


@app.route('/capturelogs/<string:appuid>', method='POST')
def capture_log(appuid):
	logData = request.data
	#send to tokenizer for processing it.
	return "Success"




