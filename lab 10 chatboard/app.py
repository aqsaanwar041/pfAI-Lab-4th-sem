from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
chat_data = {
    "admission requirements": "You need 60% marks in your previous degree to apply.",
    "deadlines": "Admission applications close on 30th December every year.",
    "program info": "We offer BS, MS, and PhD programs in Computer Science, AI, and Data Science.",
    "default": "Sorry, I didn't understand that. Please ask about admission requirements, deadlines, or program info."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_msg = request.form["message"].lower()
    for key in chat_data:
        if key in user_msg:
            return jsonify({"response": chat_data[key]})
    return jsonify({"response": chat_data["default"]})

if __name__ == "__main__":
    app.run(debug=True)
