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
        return resolve_expr(user, command_text)
    except diceroll.ParseException:
        return {
            "response_type": "in_channel",
            "text": "Slackroller cannot roll '" + command_text + "'"
        }

def resolve_expr(user, dice):
    result = roll_expr(dice)
    return {
        "response_type": "in_channel",
        "text": user + " rolled " + dice + " and got: " + str(sum(result)),
        "attachments": [
            {
                "text":roll_details(result)
            }
        ]
    }

def roll_details(result):
    parts = [annotate(part) for part in result]
    return ":mag_right: " + " + ".join(parts)

def annotate(part):
    if (part == 20):
        return "(20)"
    if (part == 1):
        return "[Jeff]"
    return str(part)

def roll_expr(text):
    if "(" in text:
        return roll_result(text)
    parts = re.split("\+", text)
    return [sum(roll_result(x)) for x in parts]

def roll_result(expr):
    result = diceroll.roll(expr)
    if isinstance(result, (int, long)):
        return [result]
    return result

if __name__ == '__main__':
    import urllib
    print handler({ "body": urllib.urlencode({
        "channel_name": "pbp", 
        "user_name": "Brian", 
        "text": sys.argv[1]})}, {})
