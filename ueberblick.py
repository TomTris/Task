import pandas as pd

name = "winequality-red.csv"
df = pd.read_csv(name, sep=";")
print()
print()
print(df)
print()