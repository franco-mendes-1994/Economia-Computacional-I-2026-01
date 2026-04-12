
# Alocação de memória

n = 0
razao = 0
a1 = 0
soma = 0
an = 0

# entrada de dados

n = int(input("Informe o número do elemento da PA que você deseja: \n"))
razao = int(input("Informe a razao  da PA: \n"))
a1 = int(input("Informe o valor do primeiro elemento da PA: \n"))

# processamento de dados

an = n*razao + a1
soma = (a1 + an)/(n/2)

# saida de dados

print(f" A{n} é igual a {an}")
print(f" A soma dos termos é igual a {soma}")