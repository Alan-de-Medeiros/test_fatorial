from function import upper_case


def test_upper_case():
    assert upper_case('Adrian') is True
    assert upper_case('adrian') is False
    assert upper_case('LETRAS GRANDES') is True
    assert upper_case('letras pequenas') is False