from flask import Blueprint, jsonify
from database import get_latest_temperatures
from schemas import TemperatureSchema

temperature_bp = Blueprint("temperature", __name__)

@temperature_bp.route('/api/temperature', methods=['GET'])
def get_temperature():
    rows = get_latest_temperatures()
    return jsonify([TemperatureSchema(temperature=row[1], timestamp=row[2]).dict() for row in rows])