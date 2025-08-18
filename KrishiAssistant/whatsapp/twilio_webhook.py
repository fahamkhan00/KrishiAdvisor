# whatsapp/twilio_webhook.py
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    user_msg = request.form.get("Body")
    resp = requests.post("http://localhost:8000/ask", json={"query": user_msg})
    reply = resp.json().get("answer", "Sorry, I couldn't process that.")
    
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
