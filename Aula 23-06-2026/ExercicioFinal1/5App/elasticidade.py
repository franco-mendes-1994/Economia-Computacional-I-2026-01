import math
import pandas as pd

def elastic(quant: pd.DataFrame, prec: pd.DataFrame) -> list:
    elastic = list()
    elastic.append(1)
    for i in range(1, len(quant)):
        aux1 = quant.iloc[i,1] / quant.iloc[0,1]
        aux2 = math.log(aux1)
        aux3 = prec.iloc[i,1] / prec.iloc[0,1]
        aux4 = math.log(aux3)
        aux5 =  aux2 / aux4
        elastic.append(aux5)
    return elastic