@app.route("/debug", methods=["POST"])
def debug():
    return jsonify({
        "files": list(request.files.keys()),
        "form": list(request.form.keys())
    })
