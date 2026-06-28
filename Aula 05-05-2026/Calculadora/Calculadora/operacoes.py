
# Processamento da adição

def soma(x, y):
    z = x + y
    return z

# Processamento da subtração

def sub(x,y):
    z = x - y
    return z


# Processamento da multiplicação

def multi(x,y):
    z = x*y
    return z

# Processamento da divisão

def div(x,y):
    if y == 0:
        z = "Nao existe divisão por zero"
    else:
        z = x/y
    return z