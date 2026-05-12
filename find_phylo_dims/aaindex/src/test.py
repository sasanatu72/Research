import pandas as pd
from aaindex import aaindex1

df = pd.read_csv("../data/aaindex2.csv", index_col=0)
df2 = pd.read_csv("../../../../aaindex/data/amino_index.csv", index_col=0)
print(df)
df2 = df2.sort_index()
print(df2)
print(df2.equals(df))
print(df.index.equals(df2.index))
print(df.columns.equals(df2.columns))
diff = (df == df2)
print(diff)
