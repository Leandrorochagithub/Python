# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A09-C02
# Cria um dataframe e exporta para .xlsx.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

data = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([11, 20, 30])
}

df = pd.DataFrame(data)

workbook = 'Numeros_Dataframe.xlsx'  #Nome da planilha
sheet = 'Aba1' #Nome da Aba

df.to_excel(workbook, sheet, index=False) #False = Sem coluna de índice
