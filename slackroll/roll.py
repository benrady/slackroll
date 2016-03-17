import sys
import logging

logger = logging.getLogger()

from urlparse import parse_qs
import diceroll

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
        "text": user + " rolled " + command_text + " and got: " + str(sum(result)),
        "attachments": [
            {
                "text":"Details: " + " + ".join([str(x) for x in result])
            }
        ]
    }

def roll_result(expr):
    result = diceroll.roll(expr)
    if isinstance(result, (int, long)):
        return [result]
    return result

if __name__ == '__main__':
    print handler({'body': sys.argv[1]}, {})
