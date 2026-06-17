from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Stress Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    return jsonify({
        "files": list(request.files.keys()),
        "form": list(request.form.keys())
    })

if __name__ == "__main__":
    app.run()
