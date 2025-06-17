from registration import register_user, authenticate_user

def test_register_user_success():
    assert register_user("ali", "1234") == True

def test_register_user_duplicate():
    register_user("ayşe", "abcd")
    assert register_user("ayşe", "abcd") == False

def test_authenticate_user_success():
    register_user("veli", "pass123")
    assert authenticate_user("veli", "pass123") == True

def test_authenticate_user_fail():
    assert authenticate_user("unknown", "1234") == False
