# esse é o controller da aplicção

import model as md
import view as vw
import dal

def main():
    dados = dal.reader()
    resultado = md.soma(dados[0], dados[1])
    # vw.impressora(dados, resultado)
    vw.print_web(dados, resultado)

if  __name__ == '__main__':
    main()
