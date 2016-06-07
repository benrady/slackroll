import diceroll

from mock import patch
from slackroll import roll 
from urllib import urlencode

def event(text="1d20 + 4"):
    return { "body": urlencode({
        "channel_name": "pbp", 
        "user_name": "Brian", 
        "text": text})}

@patch('diceroll.roll')
def test_displays_roll_result_as_text(roll_mock):
    roll_mock.side_effect = [[18], 4]
    assert roll.handler(event(), {})["text"] == "Brian rolled 1d20 + 4 and got: 22"

def test_responds_in_the_channel():
    assert roll.handler(event(), {})["response_type"] == "in_channel"
    
@patch('diceroll.roll')
def test_explains_roll_results_as_attachment(roll_mock):
    roll_mock.side_effect = [[18], 4]
    assert roll.handler(event(), {})["attachments"][0] == {"text": ":mag_right: 18 + 4"}

@patch('diceroll.roll')
def test_recognizes_critical_hits(roll_mock):
    roll_mock.side_effect = [[20], 4]
    assert roll.handler(event(), {})["attachments"][0]["text"] == ":mag_right: (20) + 4"
    #assert roll.handler(event(), {})["attachments"][0]["color"] == "#36a64f"

@patch('diceroll.roll')
def test_recognizes_critical_misses(roll_mock):
    roll_mock.side_effect = [[1], 4]
    assert roll.handler(event(), {})["attachments"][0]["text"] == ":mag_right: [Jeff] + 4"

@patch('diceroll.roll')
def test_result(roll_mock):
    roll_mock.side_effect = [[3], [2, 5], 3]
    text = 'd6 + 2d8 +   3  '
    assert roll.roll_expr(text) == [3, 7, 3]

def test_returns_help_on_error():
    assert roll.handler(event("fubar"), {})['text'] == "Slackroller cannot roll 'fubar'"

@patch('diceroll.roll')
def test_handles_parens(roll_mock):
    roll_mock.side_effect = [22]
    result = roll.handler(event("4*(2d6 + 1)"), {})
    assert result['text'] == "Brian rolled 4*(2d6 + 1) and got: 22"
    assert result['attachments'][0] == {"text": ":mag_right: 22"}
    

     
    
