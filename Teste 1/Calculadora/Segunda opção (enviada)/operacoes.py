

def soma(x,y):
    resultado = x + y
    return resultado

def diferenca(x,y):
    resultado = x - y
    return resultado

def multi(x,y):
    resultado = x * y
    return resultado

def div(x,y):
    if y == 0:
        resultado = "Você não pode dividir por zero"
    else:
        resultado = x / y
    return resultado