import pandas as pd

df = pd.read_csv("../data/aaindex.csv", index_col=0)
na_list = ["AVBF000101", "AVBF000102", "AVBF000103", "AVBF000104", "AVBF000105", "AVBF000106", "AVBF000107", "AVBF000108", "AVBF000109", "YANJ020101", "GUYH850103", "ROSM880104", "ROSM880105"]
# https://www.genome.jp/ftp/db/community/aaindex/aaindex1 より確認

df = df.drop(na_list, axis=0)
df.to_csv("../data/aaindex2.csv", header=True, index=True)
