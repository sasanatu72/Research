import numpy as np
import pandas as pd

nd5_9 = np.array(pd.read_csv("../data/ND5_9.csv", header=None))

dims = range(0, 2560) # 使用plmが2560次元のため

emb = []
amino = []
for nd5 in nd5_9:
    emb.extend(np.array(pd.read_csv(f"../data/{nd5[0]}_vec.csv", header=None)))
    amino.extend(nd5[1])
emb = np.array(emb)

amino_score = {}
amino_list = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
for dim in dims:  
    amino_score[str(dim)] = {} 
    cluster_emb = np.mean(emb[:, [dim]], axis=1)
    for amino_char in amino_list:
        index = [i for i, char in enumerate(amino) if char == amino_char]
        if len(index) > 0:
            amino_score[str(dim)][amino_char] = cluster_emb[index].mean()
        else:
            amino_score[str(dim)][amino_char] = np.nan
        
pd.DataFrame.from_dict(amino_score, orient="index").to_csv("../data/all_amino_score.csv", header=True, index=True)