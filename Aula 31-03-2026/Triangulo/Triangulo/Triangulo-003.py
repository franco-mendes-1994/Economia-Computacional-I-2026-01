"""

# Programa triângulo

Descrição: Este programa cria um triangulo

**Autor: Franco Mendes de Souza**

**Data: 31/03/2026**

**Versão: 0.0.3**

"""

# Alocação de memória

area = 0.0
base = 0.0
altura = 0.0
lado_1 = 0.0
lado_2 = 0.0
lado_3 = 0.0
parte_menor = 0.0
parte_maior = 0.0
triangulo = [lado_1, lado_2, lado_3]
i = 0

# Entrada de dados

while i < 3:
    triangulo[i] = float(input("\nDigite um lado do triângulo que você quer calcular a área: "))
    i += 1

print(triangulo)

# Processamento de dados

triangulo.sort(reverse = True)
base = triangulo[0]


# Cálculo das partes
parte_menor = triangulo[1]**2/base
parte_maior = triangulo[2]**2/base

# Cálculo da altura

altura = (parte_menor*parte_maior)**(1/2)

# Cálculo da area

area = 0.5*base*altura

# Saída de dados

print(f"A área do triangulo de lados {triangulo[0]}, {triangulo[1]} e {triangulo[2]} é igual a {area}.")