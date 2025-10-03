from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_reply(msg):
    msg = msg.lower()
    if "hello" in msg or "hi" in msg:
        return "Hi there! How can I help you?"
    if "what is ai" in msg:
        return "AI stands for Artificial Intelligence. It allows machines to learn and make decisions."
    if "pros and cons of ai" in msg:
        return ("Pros of AI: Automation, Efficiency, Data Analysis. "
                "Cons of AI: Job Displacement, Privacy Issues, Bias in Decision Making.")
    if "branches of ai" in msg:
        return ("Branches of AI include Machine Learning, Natural Language Processing, "
                "Computer Vision, Robotics, and Expert Systems.")
    if "how are you" in msg:
        return "I am doing great! How about you?"
    if "your name" in msg:
        return "I am ChatBot, your friendly assistant."
    if "time" in msg:
        return "I don't have a watch, but you can check your device time!"
    if "bye" in msg or "exit" in msg or "quit" in msg:
        return "Goodbye! Have a great day!"
    return "Sorry, I don't understand that. Try asking something else!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_reply", methods=["POST"])
def get_reply():
    user_msg = request.json.get("message")
    bot_reply = get_bot_reply(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
