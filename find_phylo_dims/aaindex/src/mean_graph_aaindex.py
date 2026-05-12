import numpy as np
import pandas as pd

id_list = np.array(pd.read_csv("../data/ND5_9.csv", header=None))[:, 0]

mean_df = pd.DataFrame()

mean_dict = {}
for name in id_list:
    mean_dict[name] = pd.read_csv(f"../data/vec/{name}_sum.csv", header=None, index_col=0).mean(axis=1)
    mean_df[name] = mean_dict[name]

mean_df.to_csv("../data/vec/mean.csv", header=True, index=True)
