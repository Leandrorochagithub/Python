# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A06-C01
# Seleção de múltiplas linhas.
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
print(df[1:3]) # Linhas 1 e 2
