
# alocação de memória

numero = 0

resultado = 0

# entrada de dados

numero = float(input("Informe o número: \n"))

# processamento de dados

if numero < 10:
    resultado = numero*2
elif numero < 20:
    resultado = numero/2
else:
    resultado = False

# saída de dados
if resultado == False:
    print(f"O número {numero} não é válido")
else:
    print(resultado)