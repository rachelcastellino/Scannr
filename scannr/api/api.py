from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/getReceipt')
def get_receipt():
    response=jsonify({'receipt':'RECEIPT INFO HERE'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

