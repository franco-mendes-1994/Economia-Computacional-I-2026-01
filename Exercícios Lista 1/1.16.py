
# alocação de memória

retorno_exp = 0

retorno_srisc = 0

retorno_mercado = 0

sensibilidade = 0

# entrada de dados

retorno_srisc = float(input("Informe o retorno da carteira sem risco: \n"))

retorno_mercado = float(input("Informe o retorno da carteira de mercado: \n"))

sensibilidade = float(input("Informe o coeficiente de sensibilidade:\n"))

# processamento dos dados

retorno_exp = retorno_srisc + sensibilidade*(retorno_mercado - retorno_srisc)

# saída dos dados

print(retorno_exp)