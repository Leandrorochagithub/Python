import pandas as pd

columns = ['UNIDADES', 'DEZENAS']

rows = [
    [1, 10],
    [2, 20]
]

df = pd.DataFrame(rows, columns=columns)

print(df)
print('--------------------')

rows2 = [
    [3, 30]
]

df2 = pd.DataFrame(rows2, columns=columns)
print(df2)
print('--------------------')

df = pd.concat([df, df2], ignore_index=True)
print(df)
