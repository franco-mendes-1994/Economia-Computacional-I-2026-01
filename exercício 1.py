
# Programa que exercício aula 17/03/2026
# Descrição:  Este programa lê dois números informados pelo usuário e calcule o resultado da subtração, da multiplicação, da divisão, da exponenciação e da radiciação
# Autor: Franco Mendes de Souza
# Data: 17/03/2026
# Versão: 0.0.1

# Alocação de memória

numero_1 = 0

numero_2 = 0

sub = 0

mult = 0

div = 0

exp = 0

rad = 0

# Entrada de dados

numero_1 = float(input("Informe o primeiro número: "))

numero_2 = float(input("Informe o segundo número: "))

# Processamento de dados

sub = numero_1 - numero_2

mult = numero_1*numero_2

div = numero_1/numero_2

exp = numero_1**numero_2

rad = numero_1**(1/numero_2)

# Saída de dados

print(f"Sendo os números {numero_1} e {numero_2}, então a subtração é {sub}, a multiplicação é {mult}, a divisão é {div}, a exponenciação é {exp} e a radiciação é {rad}")