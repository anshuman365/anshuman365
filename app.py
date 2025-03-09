from flask import Flask, render_template, request, jsonify
from api.auth import auth_bp
from api.query import query_bp
from database import init_db
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config.from_object("config")

# Initialize the database
init_db()

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(query_bp, url_prefix="/db")

# Add home route
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/db/execute", methods=["POST"])
def execute_query():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Assuming you're using SQLite, adjust the connection string as needed
        engine = create_engine('sqlite:///server.db')  # Change the connection string as needed
        
        with engine.connect() as conn:
            result = conn.execute(query)
            
            # Handling SELECT queries
            if query.strip().lower().startswith("select"):
                result_data = [dict(row) for row in result.fetchall()]
                return jsonify({"result": result_data})
            
            # Handling non-SELECT queries (INSERT, UPDATE, DELETE, CREATE, etc.)
            rows_affected = result.rowcount
            return jsonify({"result": "Query executed successfully", "rows_affected": rows_affected})

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)