

# Groq Chatbot

A web-based chatbot powered by the **Groq API** using Flask. Chat with a friendly AI through a clean, responsive UI similar to ChatGPT.


## Features

Interactive web-based chat interface

Maintains recent chat history

Reset chat functionality

Short, clear AI responses

Uses Groq API for AI-based responses

Responsive UI with smooth scrolling

## Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Libraries: Flask-CORS, Requests, Python-Dotenv, Groq

Server: Gunicorn (for production)

## Run Locally

Clone the project

```bash
 git clone https://github.com/EmaanSafdar/Groq-Chatbot.git



```

Go to the project directory

```bash
  cd Groq-Chatbot
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create a virtual environment

```bash
  python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
Create a .env file in the project root and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
```bash
python chatbot.py
```
Open your browser at http://127.0.0.1:5000 to use the chatbot.


## Deployment

To deploy this project run
Make sure your requirements.txt includes:



 flask

flask-cors

gunicorn

requests

python-dotenv

groq

Use this start command on Render or similar platforms:
 ```bash
 gunicorn chatbot:app
 ```



## Troubleshooting


ModuleNotFoundError: Add missing libraries to requirements.txt and redeploy.

Status 127 / gunicorn not found: Make sure gunicorn is in requirements.txt.

Groq API key errors: Ensure .env exists and contains GROQ_API_KEY.
## Demo

https://groq-chatbot-8.onrender.com/
