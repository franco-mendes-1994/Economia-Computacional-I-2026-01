

def leitura_dados():
    dados = [0,0]
    i = 0
    while i < 2:
        dados[i] = float(input(f"\nDigite a partela {i + 1}: "))
        i+=1
    return dados

def saída(lista: list, resultado: float) -> None:
    print(f"\nA soma da parcela {lista[0]} com a parcela {lista[1]} é igual a {resultado}")

