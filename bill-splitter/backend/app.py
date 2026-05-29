from flask import Flask, render_template, request, jsonify
from validators import validate_input
from logic import calculate_split
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Не передан JSON-тело запроса"}), 400

        errors = validate_input(data)
        if errors:
            return jsonify({"error": errors}), 400

        bill = float(data["bill"])
        tip_percent = float(data["tip_percent"])
        people = int(data["people"])

        result = calculate_split(bill, tip_percent, people)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": "Внутренняя ошибка сервера", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
