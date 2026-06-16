from flask import Flask, request, jsonify
import joblib
import librosa
import numpy as np

app = Flask(__name__)

model = joblib.load("stress_model.pkl")

def extract_features(file_name):

    audio, sample_rate = librosa.load(
        file_name,
        duration=3,
        offset=0.5
    )

    mfccs = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    mfccs_scaled = np.mean(
        mfccs.T,
        axis=0
    )

    return mfccs_scaled

@app.route("/")
def home():
    return "Stress Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    audio_file = request.files["file"]

    audio_file.save("temp.wav")

    feature = extract_features("temp.wav")

    prediction = model.predict([feature])

    return jsonify({
        "stress": str(prediction[0])
    })

if __name__ == "__main__":
    app.run()
