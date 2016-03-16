
from urlparse import parse_qs

def handler(event, context):
    req_body = event['body']
    params = parse_qs(req_body)

    user = params['user_name'][0]
    channel = params['channel_name'][0]
    command_text = params['text'][0]
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
    result = roll_result(command_text)
    return {
        "response_type": "in_channel",
        "text": user + " rolled " + command_text + " and got: " + result,
        "attachments": [
            {
                "text":"Details: 18 + 4"
            }
        ]
    }

def roll_result(expr):
    return "22"
