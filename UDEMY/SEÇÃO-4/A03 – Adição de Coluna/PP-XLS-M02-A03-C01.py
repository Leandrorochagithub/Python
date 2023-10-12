import pandas as pd

d = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([10, 20, 30])
}

df = pd.DataFrame(d)
print(df)
df['CENTENAS'] = pd.Series([100, 200, 300])
print(df)
df['SOMA'] = df['UNIDADES'] + df['DEZENAS'] + df['CENTENAS']
print(df)