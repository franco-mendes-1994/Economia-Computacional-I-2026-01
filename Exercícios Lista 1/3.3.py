
# alocação de memória

num = [0, 0, 0, 0, 0]

# entrada e processamento de dados

for i in range(5):
    num[i] = float(input(f"Informe o {i + 1}º número: \n"))
    num[i] = num[i]**2

# saída de dados

print(num)