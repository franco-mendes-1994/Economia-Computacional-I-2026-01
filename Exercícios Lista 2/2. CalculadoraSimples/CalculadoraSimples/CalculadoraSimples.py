class CalculadoraSimples:
    def __init__(self, last_result: float) -> None:
        self.last_result = last_result
    def last(self) -> float:
        return self.last_result
    def soma(self, num_1: float, num_2: float) -> float:
        aux = num_1 + num_2
        self.last_result = aux
        return aux
    def sub(self, num_1: float, num_2: float) -> float:
        aux = num_1 - num_2
        self.last_result = aux
        return aux
    def mult(self, num_1: float, num_2: float) -> float:
        aux = num_1 * num_2
        self.last_result = aux
        return aux
    def div(self, num_1: float, num_2: float) -> float:
        aux = num_1 / num_2
        self.last_result = aux
        return aux

    