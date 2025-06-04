from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os

app = Flask(__name__, static_folder="static")

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not set in environment variables")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

@app.route("/chat", methods=["POST"])
def chat_with_gemini():
    user_input = request.json.get("message")
    response = chat.send_message(user_input)
    return jsonify({"reply": response.text})

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
