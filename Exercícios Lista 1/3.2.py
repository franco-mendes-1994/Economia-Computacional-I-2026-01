
# alocação de memória

numero = 0

raiz = 1

# entrada de dados

numero = float(input("Informe o número cuja raíz deseja calcular: \n"))

# processamento de dados

for i in range(10000):
    raiz = (raiz + numero/raiz)/2

# saída de dados

print(raiz)