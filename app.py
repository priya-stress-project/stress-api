from flask import Flask, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("stress_model.pkl")

@app.route("/")
def home():
    return "Stress Prediction API Running"

@app.route("/predict")
def predict():
    result = model.predict([[0]*40])
    return jsonify({
        "model_loaded": True,
        "sample_prediction": str(result[0])
    })

if __name__ == "__main__":
    app.run()
