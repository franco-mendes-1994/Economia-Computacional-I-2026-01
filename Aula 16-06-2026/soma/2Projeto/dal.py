"""
Este módulo é a camada de acesso a dados da minha aplicação
"""

def reader():
    i = 0
    dados = [0,0]
    while i < 2:
        dados[i] = float(input(f"Digite a parcela {i + 1}: "))
        i += 1
    return dados


def writer(dados: list) -> None:
    with open('arquivo.txt', 'w', encoding = 'utf-8') as arquivo:
        conteudo = arquivo.write(str(dados))
    