

def operacao():
    operacao = input("Informe a operação matemática que deseja executar \n(Opções disponíveis: soma, diferença, multiplicação e divisão) \n(Digite FIM para parar o programa) \n")
    return operacao


def numeros():
    lista = [0,0]
    for i in range(2):
        lista[i] = complex( float(input(f"Informe a parte real do {i + 1}º número: \n")), float(input(f"Informe a parte imaginária do {i + 1}º número: \n")))
    return lista
    

def saida(numeros, operacao, resultado):
    if resultado == "Você não pode dividir por zero":
        print(resultado)
    else:
        print(f"A {operacao} de {numeros[0]} e {numeros[1]} é igual a {resultado}")