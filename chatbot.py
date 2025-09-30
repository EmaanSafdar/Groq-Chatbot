from flask import Flask, request, jsonify, render_template
from groq import Groq
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

client = Groq(api_key=groq_api_key)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"reply": "⚠️ Please type something."})

    chat_history.append({"role": "user", "content": user_input})
    trimmed_history = chat_history[-10:]

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ Groq supported
            messages=[
                {"role": "system", "content": (
                    "You are a friendly chatbot. "
                    "Give short, clear answers (2–5 lines). "
                    "Break into points if needed."
                )}
            ] + trimmed_history,
            temperature=0.6,
            max_tokens=300
        )

        bot_reply = response.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": bot_reply})

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset_chat():
    global chat_history
    chat_history = []
    return jsonify({"status": "ok", "message": "Chat cleared ✅"})


if __name__ == "__main__":
    app.run(debug=True)
