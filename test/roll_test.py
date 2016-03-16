from slackroll import roll 

def test_fail():
    assert service.handler({}, {})["text"] == "Steve rolled 22 (18 + 4)"
    
