
# alocação de memória

preco = 0
renda = 0
demanda = 0

# entrada de dados

preco = float(input("Informe o preço do bem: \n"))

renda = float(input("Informe a renda do consumidor: \n"))

# processamento de dados

demanda = renda/preco

# saída de dados

print(f"A quantidade demandada pelo consumidor com renda {renda} e ao preço {preco} é de {demanda} unidades do bem")