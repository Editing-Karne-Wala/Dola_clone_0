from twilio.twiml.messaging_response import MessagingResponse

# Create a new response object
response = MessagingResponse()
response.message("This is a test message from MessagingResponse.")

# Print the TwiML (Twilio Markup Language) XML string
print(str(response))
