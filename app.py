#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
import es_util.es_helper as es_helper
import tokenizer.tokenizer as tokenizer

app = Flask(__name__)


@app.route('/capturelogs/<string:appuid>', methods=['POST'])
def capture_log(appuid):
	logData = request.data.decode("utf-8")
	tokenized = tokenizer.process_extract_log(logData,appuid)
	print(tokenized)
	for log in tokenized:
		es_helper.create_index(appuid, log)
	return "Success"

if __name__ == '__main__':
    app.run()
