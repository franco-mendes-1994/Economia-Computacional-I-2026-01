"""
Programa adulto ou criança
Descrição: Este programa pergunta a idade de uma pessoa. Se a idade for maior ou igual a 18 anos, o programa imprime na tela "Oi! Você é um adulto.". Se não, o programa imprime "Oi! Você é menor de idade."
Autor: Franco Mendes de Souza
Data: 24/03/2026
Versão: 0.0.1
"""

# Alocação de memória

idade = 0
texto = ""

# Entrada de dados

idade = int(input("\nQual a sua idade? "))


# Processamento de dados

if idade >= 18:
    texto = "Oi! Você é um adulto."
else:
    texto = "Oi! Você é menor de idade."

# Saída de dados

print(texto)