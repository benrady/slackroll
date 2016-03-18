import diceroll

from mock import patch
from slackroll import roll 
from urllib import urlencode

def event(text="1d20 + 4"):
    return { "body": urlencode({
        "channel_name": "pbp", 
        "user_name": "Brian", 
        "text": "1d20 + 4"})}

@patch('diceroll.roll')
def test_displays_roll_result_as_text(mock):
    mock.return_value = 22
    assert roll.handler(event(), {})["text"] == "Brian rolled 1d20 + 4 and got: 22"

def test_responds_in_the_channel():
    assert roll.handler(event(), {})["response_type"] == "in_channel"
    
@patch('diceroll.roll')
def test_explains_roll_results_as_attachment(mock):
    mock.return_value = [18, 4]
    assert roll.handler(event(), {})["attachments"][0] == {"text": "Details: 18 + 4"}
