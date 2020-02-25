from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/greetings', methods=['GET'])
def get_greeting():
    return jsonify('Hello world!')
