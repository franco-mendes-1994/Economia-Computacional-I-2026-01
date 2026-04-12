# Programa que soma002
# Descrição: Este programa lê dois números digitados pelo usuário e calcula a soma deles
# Autor: Franco Mendes de Souza
# Data: 17/03/2026
# Versão: 0.0.3
# Notas da versão: Correção de erro semântico no uso da função input que produzia a concatenação de textos em vez de soma de números

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

print(soma)