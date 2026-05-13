import numpy as np
import pandas as pd

id_list = np.array(pd.read_csv("data/ND5_9.csv", header=None))[:, 0]
mean_list = []

for name in id_list:
    embbeding = np.array(pd.read_csv(f"data/{name}_vec_sum.csv", header=None))
    mean_list.append(np.mean(embbeding, axis=0))

pd.DataFrame(mean_list, dtype=float).to_csv("data/mean_vec.csv", header=False, index=False)