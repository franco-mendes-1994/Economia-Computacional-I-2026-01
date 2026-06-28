
# Definição das funções

def leitura_dados():
    dados = [0,0]
    i = 0
    while i < 2:
        dados[i] = float(input(f"\nDigite a partela {i + 1}: "))
        i+=1
    return dados

def soma(x,y):
    return x + y

def saída(lista, resultado):
    print(f"\nA soma da parcela {lista[0]} com a parcela {lista[1]} é igual a {resultado}")

def main():
    dados = leitura_dados()

    resultado = soma(dados[0], dados[1])

    saída(dados, resultado)

if __name__ == '__main__':
    main()