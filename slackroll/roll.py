import sys
import logging

logger = logging.getLogger()

from urlparse import parse_qs
from diceroll import roll

def handler(event, context):
    logger.info('got event{}'.format(event))
    req_body = event['body']
    params = parse_qs(req_body)

    user = params['user_name'][0]
    channel = params['channel_name'][0]
    command_text = params['text'][0]
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
    print roll
    return str(roll(expr))

if __name__ == '__main__':
    print handler({'body': sys.argv[1]}, {})
