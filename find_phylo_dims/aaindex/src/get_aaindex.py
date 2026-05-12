import pandas as pd
from aaindex import aaindex1

all_indices = {}

for record_id in aaindex1.record_codes():
    amino_score = aaindex1[record_id].values
    all_indices[record_id] = amino_score

df = pd.DataFrame.from_dict(all_indices, orient="index")
df = df.drop("-", axis=1)[["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]]
df.to_csv("../data/aaindex.csv", header=True, index=True)