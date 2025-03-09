from flask import Blueprint, request, jsonify
from database import execute_query

query_bp = Blueprint("query", __name__)

@query_bp.route("/execute", methods=["POST"])
def execute():
    data = request.json
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "Query missing"}), 400

    result = execute_query(query)
    return jsonify({"result": result})