import open_clean_data
import elasticidade
import output_data




def main():
    quant = open_clean_data.open_data("5App/consumo.csv")
    prec = open_clean_data.open_data("5App/preco.csv")
    clean_quant = open_clean_data.clean_data_1(quant)
    clean_prec = open_clean_data.clean_data_2(prec)
    result = elasticidade.elastic(clean_quant, clean_prec)
    return print(result)


if __name__ == '__main__':
    main()
