from flask import Flask
from flask_cors import CORS
from database import create_db
from routers import api_bp
import services.mqtt

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_bp)

if __name__ == "__main__":
    create_db()
    app.run(host="0.0.0.0", debug=True)