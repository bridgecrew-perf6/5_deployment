import joblib
from flask import Flask, request, jsonify, render_template

MODEL_PATH = "model.joblib"

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Check parameters
    if request.json:
        # Get JSON as dictionnary
        json_input = request.get_json()
        # Load model
        if "input" in json_input.keys():
            regressor = joblib.load(MODEL_PATH)
    
            prediction = regressor.predict(json_input["input"]).tolist()

            return jsonify({"the prediction is": prediction}), 200
    return jsonify({"msg": "Error, no JSON detected"})

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)