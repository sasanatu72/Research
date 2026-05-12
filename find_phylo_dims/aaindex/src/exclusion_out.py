import pandas as pd

amino_index = pd.read_csv("../data/aaindex2.csv", index_col=0)
drop = []

for i in range(len(amino_index.index)):
    line = amino_index.iloc[i]
    name = line.name

    # 四分位数
    q1 = line.describe()['25%']
    q3 = line.describe()['75%']
    
    # 四分位範囲
    iqr = q3 - q1 

    # 外れ値の基準点
    outlier_min = q1 - (iqr) * 1.5
    outlier_max = q3 + (iqr) * 1.5

    # 範囲から外れている値を除く
    if ((line > outlier_max) | (line < outlier_min)).any():
        drop.append(name)

print(len(drop))
print(drop)
out_index = amino_index.drop(drop)
print(out_index)
out_index.to_csv("../data/aaindex3.csv", header=True, index=True)