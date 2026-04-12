
# alocação de memória

a = 0

b = 0

c = 0

delta = 0

x1 = 0

x2 = 0

# entrada de dados

a = float(input("Informe o coeficiente que acompanha o termo quadrático: \n"))

b = float(input("Informe o coeficiente que acompanha o termo linear: \n"))

c = float(input("Informe o coeficiente constante: \n"))

delta = b**2 -4*a*c

# processamento de dados

x1 = -b + delta**(1/2)
x1 /= 2*a

x2 = -b - delta**(1/2)
x2 /= 2*a

# saída de dados

print(f"O valor de x1 é {x1}")
print(f"O valor de x2 é {x2}")