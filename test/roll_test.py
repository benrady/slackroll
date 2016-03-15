from slackroll import service 

def test_fail():
    assert service.handler({}, {})["text"] == "Steve rolled 22 (18 + 4)"
    
