

# Alocação de memória
salario_bruto = 0
salario_liquido = 0
descontos = 0
imposto = 0
valor_hora = 0
horas = 0

# Entrada de dados
imposto = 0.3
valor_hora = 40
horas = int(input("Informe o número total de horas trabalhadas: \n"))

# Processamento de dados
salario_bruto = horas*valor_hora

descontos = salario_bruto*imposto

salario_liquido = salario_bruto - descontos

# Saída de dados

print(f"salario bruto = {salario_bruto}")

print(f"salario liquido = {salario_liquido}")

print(f"descontos = {descontos}")