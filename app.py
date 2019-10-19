from flask import Flask, escape, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/face', methods=['POST'])
def face():
    search = request.json.get("id")
    name = request.json.get("photoBase64")
    return jsonify({"result":"ok"})