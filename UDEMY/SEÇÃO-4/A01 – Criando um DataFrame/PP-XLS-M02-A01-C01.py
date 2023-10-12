import pandas as pd

data =  { 
    'UNIDADES': pd.Series ([1,2,3]),
    'DEZENAS':  pd.Series ([10,20,30])
}

df = pd.DataFrame(data)

df ['CENTENAS'] =  pd.Series([100,200,300])
df['MILHARES'] = pd.Series([1000,2000,3000])
df['SOMA'] = df['UNIDADES'] + df['DEZENAS'] + df['CENTENAS'] + df['MILHARES']
print(df)
