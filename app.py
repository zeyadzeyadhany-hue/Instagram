from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Demo message server is running!"

@app.route("/demo", methods=["POST"])
def demo():
    data = request.get_json(silent=True) or {}
    note = data.get("note", "")

    if not isinstance(note, str) or len(note) > 200:
        return jsonify({"error": "Invalid demo message"}), 400

    print("Demo message received:", note, flush=True)
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
