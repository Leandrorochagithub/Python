# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A01-C04
# Criando um DataFrame a partir de List.
#

# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

import pandas as pd

data = [
    ['Alex', 10],
    ['Bob', 12],
    ['Clarke', 13]
]

df = pd.DataFrame(data, columns=['Nome', 'Idade'], dtype=float)

print(df)
