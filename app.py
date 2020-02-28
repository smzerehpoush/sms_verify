from flask import Flask, jsonify
import requests
import config
   
app = Flask(__name__)

@app.route('/')
def main_page():
	return "Hello World!"

@app.route("/v1/process")
def process():
	data = {"code" : 0, "message":"processed"}
	return jsonify(data),200
def send_sms():
	pass

def check_serial():
	pass

if __name__ == "__main__":
	app.run("0.0.0.0", 5000)

