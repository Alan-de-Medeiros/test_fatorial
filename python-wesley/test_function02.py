def Positivo(numero):
    return numero>0


def teste2():
    assert Positivo(5) is True
    assert Positivo(-5) is False
    