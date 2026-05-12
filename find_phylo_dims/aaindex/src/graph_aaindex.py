import numpy as np
import pandas as pd
from tqdm import tqdm

amino_index = pd.read_csv("../data/aaindex3.csv", index_col = 0).to_dict(orient="index")
nd5_9 = np.array(pd.read_csv("../data/ND5_9.csv", header=None))

for nd5 in tqdm(nd5_9, desc="ND5_9"):
    name = nd5[0]
    seq = nd5[1]

    vec_dict = {}
    sum_dict = {}
    for index_name, index in tqdm(amino_index.items(), desc="amino_index", leave=False):
        vec = []
        sum_vec = [0]
        for amino in seq:
            vec.append(index[amino])
            sum_vec.append(index[amino] + sum_vec[-1])
        vec_dict[index_name] = vec
        sum_dict[index_name] = sum_vec
    
    pd.DataFrame.from_dict(vec_dict, orient="index").to_csv(f"../data/vec/{name}.csv", header=False, index=True)
    pd.DataFrame.from_dict(sum_dict, orient="index").to_csv(f"../data/vec/{name}_sum.csv", header=False, index=True)


