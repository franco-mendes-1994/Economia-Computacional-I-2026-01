


def conjunto():
    conjunto = input("Informe o conjunto numérico (Opções disponíveis: reais, complexos): \n")
    return conjunto

def conjunto_segundo():
    conjunto = input("Informe o conjunto numérico (Opções disponíveis: reais, complexos) (Digite FIM para parar o programa): \n")
    return conjunto


def operacao():
    operacao = input("Informe a operação matemática que deseja executar \n(Opções disponíveis: soma, diferença, multiplicação e divisão): \n")
    return operacao


def numeros(conjunto):
    lista = [0,0]
    if conjunto == "complexos":
        for i in range(2):
            lista[i] = complex( float(input(f"Informe a parte real do {i + 1}º número: \n")), float(input(f"Informe a parte imaginária do {i + 1}º número: \n")))
    else:
        for i in range(2):
            lista[i] = float(input(f"Informe o {i + 1}º valor: \n"))
    return lista
    

def saida(numeros, operacao, resultado):
    if resultado == "Você não pode dividir por zero":
        print(resultado)
    else:
        print(f"A {operacao} de {numeros[0]} e {numeros[1]} é igual a {resultado}")