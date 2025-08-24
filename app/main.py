from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "Welcome to DevOps Mega Project"})

@app.route("/")
def welcome():
    return jsonify({"message": "This is the homepage of DevOps Mega Project"})

if __name__ == "__main__":
    # Must use 0.0.0.0 for Docker
    app.run(host="0.0.0.0", port=8000, debug=True)


