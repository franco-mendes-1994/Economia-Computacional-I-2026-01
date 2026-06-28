

def soma(x: float, y: float) -> float:
    return x + y

def mult(x: float, y: float) -> float:
    """ Esta função multiplica dois número de tipo flutuante e retorna o produto"""
    return x*y

def div(x: float, y: float) -> float:
    if y == 0:
        resultado = "Não é possível dividir por zero"
    else:
        resultado = x/y
    return resultado

def sub(x: float, y: float) -> float:
    return x - y