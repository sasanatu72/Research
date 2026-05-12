import numpy as np
import pandas as pd 

emb_amino_score = (pd.read_csv("../data/all_amino_score.csv", index_col=0)).T.to_dict(orient="list")
aaindex_amino_score = (pd.read_csv("../aaindex/data/aaindex3.csv", index_col=0)).T.to_dict(orient="list")


corr = {}
for dim, score1 in emb_amino_score.items():
    corr[str(dim)] = {}
    for index_name, score2 in aaindex_amino_score.items():
        corr[str(dim)][index_name] = np.abs(np.corrcoef(score1, score2)[0, 1])

print(len(corr.keys()))
for dim, corr_dict in corr.items():
    sorted_list = sorted(corr_dict.items(), key=lambda x:x[1], reverse=True)
    pd.DataFrame(sorted_list).to_csv(f"../data/corr_aaindex/corr_aaindex_{dim}.csv", header=False, index=False)
