from flask import Flask
import joblib

app = Flask(__name__)

model = joblib.load("stress_model.pkl")

@app.route("/")
def home():
    return "Stress API + Model Loaded Successfully"

if __name__ == "__main__":
    app.run()
