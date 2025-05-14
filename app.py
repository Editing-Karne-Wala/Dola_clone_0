from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from llama_cpp import Llama
from Calendar import create_calendar_event
import re
from datetime import datetime, timedelta

app = Flask(__name__)

# Initialize the Mistral model (adjust the path if necessary)
llm = Llama(model_path=r"C:\Users\shiny\Downloads\AI\mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

# Function to parse Mistral output and extract event details
def parse_event_from_mistral_output(response_text):
    try:
        print(f"Parsing Mistral output: {response_text}")  # Debugging line
        # Updated regex to match event name with or without single quotes
        match = re.search(r"called\s*(?:'(.*?)'|([^\n]+))\s*on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2})", response_text)
        if not match:
            print("No event details found in Mistral response.")
            return None

        # Extracted values
        title = match.group(1) or match.group(2)  # Either from quotes or plain text
        date_str = match.group(3)
        time_str = match.group(4)
        start_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        end_time = start_time + timedelta(hours=1)

        event_details = {
            "summary": title,
            "start": start_time.isoformat(),
            "end": end_time.isoformat()
        }
        print(f"Parsed event details: {event_details}")  # Debugging line
        return event_details
    except Exception as e:
        print(f"Parsing failed: {e}")
        return None

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    print(f"Received values: {request.values}")  # Log all incoming data
    incoming_msg = request.values.get('Body', '').strip()
    print(f"Received message: {incoming_msg}")  # Log the message content
    
    if not incoming_msg:
        print("No message content received.")
        return "Message content is empty."

    try:
        # Generate Mistral response
        print("Generating Mistral response...")  # Debugging line
        response = llm.create_chat_completion(
            messages=[{"role": "user", "content": f"Schedule assistant: {incoming_msg}\nResponse:"}],
            max_tokens=256
        )
        print(f"Full Mistral response: {response}")  # Log the full response object
        reply_text = response['choices'][0]['message']['content'].strip()
        print(f"Response from Mistral: {reply_text}")  # Debugging line

    except Exception as e:
        reply_text = f"❌ Mistral Error: {e}"
        print(f"Error generating response: {reply_text}")  # Debugging line

    # Parse and schedule event if event details are valid
    event_details = parse_event_from_mistral_output(reply_text)
    if event_details:
        confirmation = create_calendar_event(event_details)
        reply_text = f"📅 Event Created: {confirmation}"
        print(f"Event creation confirmation: {confirmation}")  # Debugging line

    # Send WhatsApp reply
    print(f"Sending reply to WhatsApp: {reply_text}")  # Debugging line
    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
