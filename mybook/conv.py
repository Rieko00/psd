import pandas as pd

with open('tes.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('cuaca.csv', encoding='utf-8', index=False)