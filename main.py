from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load whitelist from JSON file
with open(os.path.join(os.path.dirname(__file__), 'whitelist.json'), 'r') as f:
    whitelist_data = json.load(f)
whitelisted_users = whitelist_data.get("whitelisted_users", [])

@app.route("/api/check", methods=["GET"])
def check_user():
    username = request.args.get("username")
    if not username:
        return jsonify({"status": "error", "message": "Username not provided"}), 400

    if username in whitelisted_users:
        return jsonify({"status": "whitelisted"})
    else:
        return jsonify({"status": "not_whitelisted"})

@app.route("/")
def home():
    return "Whitelist API is running!"
