# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A05-C01
# Seleção de linha pela label.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

d = {
    'DEZENAS': pd.Series(
        [10, 20, 30],
        index=['a', 'b', 'c']
    ),
    'CENTENAS': pd.Series(
        [100, 200, 300],
        index=['a', 'b', 'c']
    )
}

df = pd.DataFrame(d)

print(df)
print('--------------------')
print(df.loc['b'])
