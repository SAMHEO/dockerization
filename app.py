from flask import Flask, jsonify, request, make_response
import sys
import time
app = Flask(__name__)

blabs = []

@app.route('/')
def get_greetings():
    return "Hello World!"

@app.route('/blabs/<id>', methods=['DELETE'])
def delete_blabs(id):
    response = "Blab not found"
    # response = blabs[0]

    for i in range(len(blabs)):
        if blabs[i]["id"] == int(id):
            del blabs[i]
            response = "Blab succesfully removed"
            break

    return response

@app.route('/blabs', methods=['GET'])
def get_blabs():
    created = request.args.get('createdSince')
    if created:
        result = []
        for i in range(len(blabs)):
            print(created)
            if blabs[i]["postTime"] > float(created):
                result.append(blabs[i])
        return jsonify(result)
    else :
        return jsonify(blabs)
    
@app.route('/blabs', methods=['POST'])
def post_blabs():
    content = request.json
    author = content['author']
    email = author['email'] 
    name = author['name']
    message = content['message']

    newBlab = {
        "id" : len(blabs) + 1,
        "postTime" : time.time(),
        "author" : {
            "email" : email,
            "name" : name
        },
        "message" : message
    }
    blabs.append(newBlab)
    return make_response(jsonify(newBlab), 201)
