from function import email_validate

def test_email_validate():
    assert email_validate("adiran@hotmail.com") is True
    assert email_validate('adrian.com') is False
