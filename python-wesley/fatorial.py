def fatorial(factor):
  
    aux= factor
    total=factor
    while aux > 1:
        total*= aux-1
        aux -= 1

    return total
        