
def handler(event, context):
    #token=gIkuvaNzQIHg97ATvDxqgjtO
    #team_id=T0001
    #team_domain=example
    #channel_id=C2147483705
    #channel_name=test
    #user_id=U2147483697
    #user_name=Steve
    #command=/roll
    #text=d20 + 4
    #response_url=https://hooks.slack.com/commands/1234/5678
    return {
        "response_type": "in_channel",
        "text": "Steve rolled 22 (18 + 4)",
        "attachments": [
            {
                "text":"Partly cloudy today and tomorrow"
            }
        ]
    }
