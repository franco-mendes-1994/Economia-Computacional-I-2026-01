

import es
import operacoes

def main():
    cont = 0
    continua = True
    while continua == True:
        if cont == 0:
            conjunto_numerico = es.conjunto()
            cont += 1
        else:
            conjunto_numerico = es.conjunto_segundo()
        if conjunto_numerico == "FIM":
            print("Obrigado por usar a calculadora!")
            break
        valores = es.numeros(conjunto_numerico)
        op = es.operacao()
        if op == "soma":
            resultado = operacoes.soma(valores[0], valores[1])
        elif op == "diferença":
            resultado = operacoes.diferenca(valores[0], valores[1])
        elif op == "multiplicação":
            resultado = operacoes.multi(valores[0], valores[1])
        else:
            resultado = operacoes.div(valores[0], valores[1])
        es.saida(valores, op, resultado)

if __name__ == '__main__':
    main()