import streamlit as st

def impressora(dados: list, resultado: float) -> None:
    """Esta função imprime na tela"""
    print(f'A soma dos números {dados[0]} e {dados[1]} é igual a {resultado}')

def print_web(dados, resultado) -> None:
    st.write(str(dados), str(resultado))
    


def printer():
    """Esta função imprime na impressora."""
    pass

