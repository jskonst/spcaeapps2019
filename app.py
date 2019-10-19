from flask import Flask, escape, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from pymongo import MongoClient
client = MongoClient('mongodb://%s:%s@127.0.0.1:27017' % ("root", "example"))
db = client["users"]
coll = db["users"]

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    coll = db["test"]
    return jsonify({"res": coll})


@app.route('/create', methods=['POST'])
def create_user():
    photo = request.json.get("photoBase64")
    name = request.json.get("name")
    user = {
        "photoBase64": photo,
        "name": name
    }
    usr = coll.insert_one(user)
    return jsonify({"result":"ok"})


@app.route('/check', methods=['POST'])
def get_user():
    photo = request.json.get("photoBase64")
    user = {
        "photoBase64": photo
    }
    dbUser = coll.find_one({"photoBase64": photo})
    if dbUser:
        return jsonify({"result": dbUser.name})
    else: 
        return jsonify({"error": "user not found"})