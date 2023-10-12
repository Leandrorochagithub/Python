# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A01-C05
# Criando um DataFrame a partir de Dicionários de Lists.
#

# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

import pandas as pd

data = {
    'Nome': ['Tomé', 'João', 'Paulo', 'Pedro'],
    'Idade': [28, 34, 29, 42]
}

df = pd.DataFrame(data)

print(df)
