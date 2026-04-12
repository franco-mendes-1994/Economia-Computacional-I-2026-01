
# alocação de memória

horas = 0

valor_hora = 0

aliquota = 0

descontos = 0

salario_auxiliar = 0

salario_final = 0

# entrada de dados

horas = float(input("Informe o total de horas trabalhadas: \n"))

valor_hora = 20

# processamento de dados

salario_auxiliar = horas*valor_hora

if 1000 < salario_auxiliar <= 2500:
    aliquota = 0.1
elif 2500 < salario_auxiliar <= 5000:
    aliquota = 0.2
elif 5000 < salario_auxiliar:
    aliquota = 0.35

desconto = salario_auxiliar*aliquota

salario_final = salario_auxiliar - desconto

# saída de dados

print(f"O salário líquido é {salario_final}")

