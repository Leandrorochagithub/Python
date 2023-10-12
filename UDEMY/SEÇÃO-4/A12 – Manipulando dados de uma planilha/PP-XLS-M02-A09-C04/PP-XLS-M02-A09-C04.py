# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A09-C04
# Lê os dados de um .xlsx, manipula e cria um outro
# arquivo .xlsx com os dados manipulados.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

df = pd.read_excel('origem.xlsx')
df['MILHAR'] = pd.Series([1000, 2000, 3000])

df.to_excel('destino.xlsx', sheet_name='Numeros', index=False)
