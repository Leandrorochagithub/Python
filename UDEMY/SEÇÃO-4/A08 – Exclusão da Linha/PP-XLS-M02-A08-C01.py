# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A08-C01
# Excluindo linhas.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

df = pd.DataFrame(
    [
        [1, 10],
        [2, 20],
        [3, 30],
        [4, 40]
    ],
    columns=['UNIDADES', 'DEZENAS']
)

print(df)
print('--------------------')

# Exclui as linhas com label 0
df = df.drop(0)

print(df)
