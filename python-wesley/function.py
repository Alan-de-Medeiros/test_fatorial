def email_validate(email):
    return '@' in email and '.com' in email 


def upper_case(text):
    return any(aux.isupper() for aux in text)