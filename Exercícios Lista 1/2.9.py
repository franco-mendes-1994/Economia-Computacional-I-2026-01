
# alocação de memória

altura = 0

peso = 0

imc = 0

categoria = ""

# entrada de dados

altura = float(input("Informe sua altura: \n"))

peso = float(input("Informe seu peso: \n"))

# processamento de dados

imc = peso/(altura**2)

if imc <= 18.5:
    categoria = "Excessivamente magro"
elif imc <= 25:
    categoria = "Peso normal"
elif imc <= 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"

# saída de dados

print(categoria)