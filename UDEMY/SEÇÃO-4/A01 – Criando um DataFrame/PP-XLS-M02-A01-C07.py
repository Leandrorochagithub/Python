# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A01-C07
# Criando um DataFrame a partir de Dicionários de Series.
#

# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

import pandas as pd

d = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([10, 20, 30])
}

df = pd.DataFrame(d)

print(df)
