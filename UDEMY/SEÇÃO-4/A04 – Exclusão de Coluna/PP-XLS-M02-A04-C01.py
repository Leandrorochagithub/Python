# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A04-C01
# Exclusão de coluna.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

d = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([10, 20, 30]),
    'CENTENAS': pd.Series([100, 200, 300])
}

df = pd.DataFrame(d)
print('O dataFrame completo é:')
print(df)

print('Excluindo as UNIDADES usando a função del()')
del(df['UNIDADES'])
print(df)

print('Excluindo as DEZENAS usando a função pop()')
df.pop('DEZENAS')
print(df)
