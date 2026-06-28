# Projeto v 0.0.1

## Projeto de interface com o usuário

A interface final será no web browser, intermediado pela biblioteca streamlit.

## Tipo de aplicação e projeto de arquitetura

A aplicação conterá quatro módulos, como listados abaixo:

1. __main__
2. open_clean_data
3. elasticidade
4. output_data

Para o desenvolvimento do módulo dois será utilizado a bibioteca pandas. Para o desenvolvimento do quarto pacote será utilizado a biblioteca streamlit

## Projeto de dados e algoritmos

O módulo open_clean_data conterá três funções, uma para abrir os dados em csv, outras duas para compatibilizar os dados entre os dois dataframes

O módulo elasticidade deverá gerar uma lista contendo as elasticidades, com a elasticidade de cada ano sendo calculada pela fórmnula simplificada oferecida pelo professor nelson. Essa fórmula está definida abaixo:

elasticidade = ln (q/q0) / ln (p/p0)

O módulo output_data utilizará a biblioteca streamlit para apresentar os dados no web browser.