from CalculadoraSimples import CalculadoraSimples

def main():
    num = CalculadoraSimples(0)
    comand = input("Informe a operação que deseja executar (Opções disponíveis: soma, subtração, multiplicação, divisão. Digite last para obter o último resultado): ")
    if comand =="soma":
        res = num.soma(float(input("Informe o primeiro número: ")), float(input("Informe o segundo número: ")))
        print(res)
    elif comand == "subtração":
        res = num.sub(float(input("Informe o primeiro número: ")), float(input("Informe o segundo número: ")))
        print(res)
    elif comand == "multiplicação":
        res = num.mult(float(input("Informe o primeiro número: ")), float(input("Informe o segundo número: ")))
        print(res)
    elif comand == "divisão":
        res = num.div(float(input("Informe o primeiro número: ")), float(input("Informe o segundo número: ")))
        print(res)
    elif comand == "last":
        print(num.last())
    else:
        print("Comando inválido")
    

if  __name__ == '__main__':
    main()
