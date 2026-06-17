@app.route("/predict", methods=["POST"])
def predict():

    return jsonify({
        "files": list(request.files.keys()),
        "form": list(request.form.keys())
    })
