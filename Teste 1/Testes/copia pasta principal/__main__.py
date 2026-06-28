

import es
import operacoes

def main():
    continua = True
    while continua == True:
        op = es.operacao()
        if op == "FIM":
            print("Obrigado por usar a calculadora!")
            break
        valores = es.numeros()
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