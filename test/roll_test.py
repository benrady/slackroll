from slackroll import roll 

def test_fail():
    assert roll.handler({}, {})["text"] == "Steve rolled 22 (18 + 4)"
    
