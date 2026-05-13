import numpy as np
import pandas as pd

id_list = np.array(pd.read_csv("data/graph9.csv", header=None))[:, 0]


for id in id_list:
    vec_sum = np.array([np.zeros(2560)], dtype=object)
    embedding = np.array(pd.read_csv(f"data/{id}_vec.csv", header=None))
    for i, vec in enumerate(embedding):
        vec_sum = np.vstack([vec_sum, vec_sum[i] + vec])
    pd.DataFrame(vec_sum, dtype=float).to_csv(f"data/{id}_vec_sum.csv", header=False, index=False)

