from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Stress Prediction API Running"

@app.route("/predict")
def predict():
    return "Predict API Ready"

if __name__ == "__main__":
    app.run()
