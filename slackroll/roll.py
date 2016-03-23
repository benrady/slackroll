import sys
import logging

logger = logging.getLogger()

from urlparse import parse_qs
import diceroll
import re

def handler(event, context):
    logger.info('got event{}'.format(event))
    req_body = event['body']
    params = parse_qs(req_body)

    user = params['user_name'][0]
    channel = params['channel_name'][0]
    command_text = params['text'][0]
    try:
        result = roll_expr(command_text)
        return {
            "response_type": "in_channel",
            "text": user + " rolled " + command_text + " and got: " + str(sum(result)),
            "attachments": [
                {
                    "text":roll_details(result)
                }
            ]
        }
    except diceroll.ParseException:
        return {
            "response_type": "in_channel",
            "text": "Slackroller cannot roll '" + command_text + "'"
        }

def roll_details(result):
    parts = [annotate(part) for part in result]
    return ":mag_right: " + " + ".join(parts)

def annotate(part):
    if (part == 20):
        return "(20)"
    if (part == 1):
        return "[1]"
    return str(part)

def roll_expr(text):
    parts = re.split("\+", text)
    return [sum(roll_result(x)) for x in parts]

def roll_result(expr):
    result = diceroll.roll(expr)
    if isinstance(result, (int, long)):
        return [result]
    return result

if __name__ == '__main__':
    print handler({'body': sys.argv[1]}, {})
