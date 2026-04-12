
# alocação de memória

capital = 0

prazo = 0

taxa = 0

montante_final = 0

# entrada de dados

capital = float(input("Informe o capital inicial investido: \n"))

prazo = int(input("Informe o prazo do investimento: \n"))

taxa = float(input("Informe a taxa de juros do investimento: \n"))

# processamento de dados

taxa /= 100

montante_final = capital*((1 + taxa)**prazo)

# saida de dados

print(f"O valor do montante final obtido no investimento é de R$ {montante_final}")