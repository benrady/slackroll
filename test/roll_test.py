import diceroll
from slackroll import roll 

event = { 
        "body": "channel_name=pbp&user_name=Brian&text=1d20%20%2B%204",
        }

def test_displays_roll_result_as_text(mocker):
    mocker.patch('diceroll.roll', new="22")
    assert roll.handler(event, {})["text"] == "Brian rolled 1d20 + 4 and got: 22"

def test_responds_in_the_channel():
    assert roll.handler(event, {})["response_type"] == "in_channel"
    
def test_explains_roll_results_as_attachment():
    assert roll.handler(event, {})["attachments"][0] == {"text": "Details: 18 + 4"}
