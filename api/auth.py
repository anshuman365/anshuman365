from flask import Blueprint, request, jsonify
from security import hash_password, verify_password

auth_bp = Blueprint("auth", __name__)

users = {"admin": hash_password("admin123")}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in users and verify_password(users[username], password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401