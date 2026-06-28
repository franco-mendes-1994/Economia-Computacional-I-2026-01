

import es
from aritmetico import soma
from Matemática.Conjuntos import inteiros

def main():
    dados = es.leitura_dados()

    resultado = soma(dados[0], dados[1])

    es.saída(dados, resultado)

if __name__ == '__main__':
    main()



