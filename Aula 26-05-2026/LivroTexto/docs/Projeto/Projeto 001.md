# Projeto v. 0.0.1

## Projeto de interface com o usurário

<!-- A partir dos requisitos, criar uma interface com o usuário, seja ela de texto (isto é, disponível no terminal de linhas de comando), seja ela gráfica. -->

A interface será de linha de comando.

## Tipo de aplicação e projeto de arquitetura

<!-- O tipo de aplicação define a melhor arquitetura, e esta por sua vez define o paradigma de programação mais adequado a ser usado. As decisões aqui tomadas dizem respeito à organização do código em funções, métodos, classes, módulos, subpacotes e pacotes. Aqui também se pode definir a melhor linguagem de programação a ser utilizadas -->

A aplicação conterá dois módulos Python, ambos dentro de um único pacote. Os nomes dos módulos serão os seguintes:

1. __main__
2. LivroTexto

## Projeto de dados e algoritmos

<!-- Os dados deverão ser alocados em estruturas de dados nativas ou em classes criadas pelo programador.Os algoritmos estarão implementados nas funções ou métodos, a depender do paradigma de programação utilizado. -->

A classe LivroTexto deverá conter os seguintes atributos e tipos:
1. titulo: str
2. autor: str
3. preco: float

Haverá um método com a seguinte assinatura:

desconto(preco: float) -> float
