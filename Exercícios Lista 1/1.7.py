
# Alocação de memória

n = 0
razao = 0
a1 = 0
soma = 0
an = 0

# entrada de dados

n = int(input("Informe o número do elemento da PG que você deseja: \n"))
razao = int(input("Informe a razao  da PG: \n"))
a1 = int(input("Informe o valor do primeiro elemento da PG: \n"))

# processamento de dados

an = a1*(razao**(n - 1))
if n == 1:
    soma = a1
else:
    soma = (a1*((razao**n) - 1))/(razao - 1)

# saida de dados

print(f" A{n} é igual a {an}")
print(f" A soma dos termos é igual a {soma}")