from flask import Blueprint
from .temperature import temperature_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(temperature_bp)
