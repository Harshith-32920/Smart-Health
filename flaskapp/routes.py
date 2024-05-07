from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "AI Health Pro API Active"})

@main.route('/predict/diabetes', methods=['POST'])
@login_required
def predict_diabetes():
    data = request.json
    # Model inference integration target
    return jsonify({"status": "success", "prediction": 0})
