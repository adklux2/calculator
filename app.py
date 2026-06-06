from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        # Only allow safe characters
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in expression):
            return jsonify({"result": "Error"})
        result = eval(expression)
        return jsonify({"result": result})
    except Exception:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(debug=True)
