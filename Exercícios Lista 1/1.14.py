
# alocação de memória

x1 = 0
x2 = 0

y1 = 0
y2 = 0

distancia = 0

# entrada de dados

x1 = float(input("Informe a coordenada x do primeiro ponto: \n"))

x2 = float(input("Informe a coordenada y do primeiro ponto: \n"))

y1 = float(input("Informe a coordenada x do segundo ponto: \n"))

y2 = float(input("Informe a coordenada y do segundo ponto: \n"))

# processamento de dados

distancia = ((x1 - y1)**(1/2) + (x2 - y2)**(1/2))**(1/2)

# saída de dados

print(f"A distância entre os pontos ({x1},{x2}) e ({y1},{y2}) é {distancia}")