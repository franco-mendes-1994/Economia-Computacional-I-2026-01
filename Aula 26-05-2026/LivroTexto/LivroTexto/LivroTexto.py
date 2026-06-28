class LivroTexto:
    def __init__(self, titulo: str, autor: str, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
    def valor_desconto(self, percentual_desconto: float) -> float:
        return self.preco*percentual_desconto
        

