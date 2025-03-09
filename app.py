from flask import Flask
from api.auth import auth_bp
from api.query import query_bp
from database import init_db

app = Flask(__name__)
app.config.from_object("config")

# Initialize database
init_db()

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(query_bp, url_prefix="/db")

if __name__ == "__main__":
    app.run(debug=True)