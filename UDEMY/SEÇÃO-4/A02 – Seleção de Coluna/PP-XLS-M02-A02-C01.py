# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A02-C01
# Seleção de coluna.
#

# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

import pandas as pd

data = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([10, 20, 30])
}

df = pd.DataFrame(data)

print(df)
print('')
print( df['UNIDADES'] )