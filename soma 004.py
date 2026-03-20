
# Programa que soma002
# Descrição: Este programa lê dois números digitados pelo usuário e calcula a soma deles
# Autor: Franco Mendes de Souza
# Data: 17/03/2026
# Versão: 0.0.4
# Notas da versão: Ediçao da função print na saída de dados, formatando a saída

# Alocação de memória

numero_1 = 0

numero_2 = 0

soma = 0

# Entrada de dados

numero_1 = int(input("Qual a primeira parcela? ")) # acrescimo da função int()

numero_2 = int(input("Qual a segunda parcela? ")) # acrescimo da função int()

# Processamento de dados: Cálculo da soma

soma = numero_1 + numero_2

# Saída de dados

print(f"A soma de {numero_1} mais {numero_2} é {soma}")