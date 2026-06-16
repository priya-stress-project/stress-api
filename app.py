@app.route("/predict", methods=["POST"])
def predict():

    audio_file = request.files["file"]

    filename = audio_file.filename

    audio_file.save(filename)

    feature = extract_features(filename)

    prediction = model.predict([feature])

    return jsonify({
        "stress": str(prediction[0])
    })
