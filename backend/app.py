from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../frontend'))
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
        "diet": "Stay hydrated, avoid caffeine excess.",
        "exercise": "Try light yoga or stretching."
    }
}

# ---------------- API ----------------
@app.route('/get-health-data', methods=['POST'])
def get_health_data():
    data = request.get_json()
    disease = data.get('disease', '').lower()

    if disease in HEALTH_DATA:
        return jsonify(HEALTH_DATA[disease])
    else:
        return jsonify({
            "advice": "No data available",
            "diet": "No data available",
            "exercise": "No data available"
        })

# ---------------- FRONTEND ----------------
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_files(path):
    return app.send_static_file(path)

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)