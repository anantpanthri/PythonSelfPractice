from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfb2480909d38b1c436557b6e56764032"
# Your Auth Token from twilio.com/console
auth_token  = "3f7837ec21c131686995b63d4b4e4dcf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14699316986", 
    from_="+16267225141",
    body="Congratulations Miss Priyanka Pande. You are our lucky Twilio winner and have just won two ticket to Ryan Adams concert on May 10 - 7:30 PM, Blue Hills Bank Pavilionto, Bring your loved ones to this event and also enjoy a complimentary dinner at the Renaissance Boston Waterfront Hotel- ASP")

print(message.sid)
