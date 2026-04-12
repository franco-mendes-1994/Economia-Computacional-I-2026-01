
# alocação de memória

num = [0,0,0,0,0,0]

num_cub = [0,0,0,0,0,0]

num_cub_root = [0,0,0,0,0,0]

# entrada de dados

for i in range(6):
    num[i] = float(input(f"Informe o {i + 1}º número: \n"))

# processamento de dados

for i in range(6):
    num_cub[i] = num[i]**3
    num_cub_root[i] = num[i]**(1/3)

# saída de dados

print(num_cub)
print(num_cub_root)