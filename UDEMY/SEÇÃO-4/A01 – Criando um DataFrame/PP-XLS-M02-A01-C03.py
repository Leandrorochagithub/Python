import pandas as pd

data = [
    ['Alex', 10],
    ['Bart', 12],
    ['Caio', 13]
]

df = pd.DataFrame(data, columns=['Nome', 'Idade'])

print(df)
