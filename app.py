from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    user_input_lower = user_input.lower() if user_input else ""

    if "hello" in user_input_lower or "hi" in user_input_lower:
        response = "Hello! How can I assist you today?"
    elif "help" in user_input_lower:
        response = "Sure, I can help! Please tell me what you need."
    elif "bye" in user_input_lower:
        response = "Goodbye! Have a great day!"
    elif "thank" in user_input_lower:
        response = "You're welcome!"
    elif "your name" in user_input_lower:
        response = "I am your support assistant."
    elif "time" in user_input_lower:
        response = f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "date" in user_input_lower:
        response = f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    elif "how are you" in user_input_lower:
        response = "I'm just a bot, but I'm doing great! How can I help you?"
    elif "services" in user_input_lower:
        response = "We offer customer support, account assistance, and more."
    elif "issue" in user_input_lower or "problem" in user_input_lower:
        response = "I'm sorry to hear that. Could you please describe the issue in detail?"
    elif "location" in user_input_lower or "where" in user_input_lower:
        response = "We are based online and available to assist you anywhere, anytime!"
    elif "contact" in user_input_lower or "email" in user_input_lower:
        response = "You can reach us at support@example.com."
    elif "price" in user_input_lower or "cost" in user_input_lower:
        response = "Our pricing details are available on the official website. Do you want the link?"
    elif "support" in user_input_lower:
        response = "Sure! I'm here to provide customer support. Please tell me your query."
    else:
        response = "I'm sorry, I didn't understand that. Could you please rephrase?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
