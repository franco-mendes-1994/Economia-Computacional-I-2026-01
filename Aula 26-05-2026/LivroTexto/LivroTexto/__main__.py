from LivroTexto import LivroTexto

def main():
    """Esta é a função principal da aplicação que consome a API do módulo LivroTexto"""
    menezes = LivroTexto("Introdução à Programação com Python", "Nilo", 200)
    print(menezes.preco)
    print(menezes.valor_desconto(0.10))

if __name__ == '__main__':
    main()

