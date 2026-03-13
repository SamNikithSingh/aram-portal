from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ARAM backend running"

@app.route("/find-schemes", methods=["POST"])
def find_schemes():

    data = request.json

    age = data.get("age")
    gender = data.get("gender")

    print("User Data:", age, gender)

    result = [
        {
            "name": "Widow Pension Scheme",
            "category": "Women Welfare",
            "description": "Monthly financial assistance"
        }
    ]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)