from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# ---------------- INIT ----------------
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# ---------------- DATA ----------------
HEALTH_DATA = {
    "fever": {
        "advice": "Drink plenty of fluids, take rest, and monitor temperature.",
        "diet": "Eat light foods like soups, fruits, and stay hydrated.",
        "exercise": "Avoid heavy exercise. Take rest."
    },
    "cold": {
        "advice": "Take warm fluids and rest. Use steam inhalation.",
        "diet": "Warm soups, ginger tea, and vitamin C foods.",
        "exercise": "Light walking only."
    },
    "headache": {
        "advice": "Drink water, relax, and avoid screens.",
        "diet": "Stay hydrated, avoid excess caffeine.",
        "exercise": "Try light yoga or stretching."
    }
}

# ---------------- API ----------------
@app.route('/get-health-data', methods=['POST'])
def get_health_data():
    data = request.get_json()

    if not data or 'disease' not in data:
        return jsonify({"error": "Disease is required"}), 400

    disease = data['disease'].lower()

    if disease in HEALTH_DATA:
        return jsonify(HEALTH_DATA[disease])
    else:
        return jsonify({
            "advice": "No data available",
            "diet": "No data available",
            "exercise": "No data available"
        })

# ---------------- FRONTEND ROUTES ----------------
@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

# ---------------- RUN ----------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)