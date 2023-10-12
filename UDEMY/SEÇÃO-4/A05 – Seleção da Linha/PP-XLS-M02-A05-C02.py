# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A05-C02
# Seleção de linha pela sua localização do índice.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

d = {
    'DEZENAS': pd.Series([10, 20, 30]),
    'CENTENAS': pd.Series([100, 200, 300, 400])
}

df = pd.DataFrame(d)
print(df)
print('--------------------')
print(df.iloc[1])
