from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["GET", "POST"])
def whatsapp():
    if request.method == "GET":
        # This helps confirm the endpoint is reachable in a browser
        return "WhatsApp endpoint is live ✅"

    # POST request: this handles messages sent from Twilio
    incoming_msg = request.form.get("Body")  # Message content
    from_number = request.form.get("From")   # Sender's number
    print(request.form)

    # Log the incoming message for debugging
    print(f"Message received: {incoming_msg} from {from_number}")

    # Create a TwiML response to send back
    response = MessagingResponse()
    response.message("Message received successfully.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
