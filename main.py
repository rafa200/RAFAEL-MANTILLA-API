from flask import Flask, request, jsonify
from datos.personas import personas

app = Flask(__name__)

@app.route("/personas", methods=["GET"])
def get_personas():
    return jsonify(personas)

if __name__ == "__main__":
    app.run(debug=True)