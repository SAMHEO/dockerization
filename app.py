from flask import Flask, jsonify, request, make_response
import pymongo
from prometheus_flask_exporter import PrometheusMetrics
from bson import ObjectId
import sys
import time
app = Flask(__name__)

metrics = PrometheusMetrics(app)
by_path_counter = metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )

mongoClient = pymongo.MongoClient("mongodb://mongo:27017")
mongoCollection = mongoClient["cs2304"]["greetings"]

@app.route('/')
def get_greetings():
    return "Hello World!"

@app.route('/blabs/<id>', methods=['DELETE'])
def delete_blabs(id):
    response = mongoCollection.delete_one({ "_id": ObjectId(id) })
    if response.deleted_count:
        return make_response(response.raw_result, 200)
    else:
        return make_response(response.raw_result, 404)
    
@app.route('/blabs', methods=['GET'])
def get_blabs():
    items = []
    for item in mongoCollection.find():
        print(item)
        i = item.copy()
        i["id"] = str(item["_id"])
        del i["_id"]
        items.append(i)
    return jsonify(items)

@app.route('/blabs', methods=['POST'])
@by_path_counter
def post_blabs():
    content = request.json
    author = content['author']
    email = author['email'] 
    name = author['name']
    message = content['message']

    newBlab = {
        "postTime" : time.time(),
        "author" : {
            "email" : email,
            "name" : name
        },
        "message" : message
    }
    response = mongoCollection.insert_one({ "blab": newBlab})
    return jsonify({ "blab" : newBlab , "id" : str(response.inserted_id)}) 