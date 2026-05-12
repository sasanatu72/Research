import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
from itertools import groupby

def check_rf0_group(data, target, n):
    count = 0
    for i, x in enumerate(data):
        if x == target:
            count += 1
            if count >= n:
                sum_aminoindex.append(i-9)
                return True
        else:
            count = 0
    return False


all_dim = range(0, 2560)
sum_aminoindex = []

rf_count = []
dim_list = []
stable_dim_list = []
for dim in all_dim:
    rf = (pd.read_csv(f"../data/RF_aaindex/RF_aaindex_{dim}.csv", header=None)).iloc[:, 0].tolist()
    rf_count.append(min(rf))
    if min(rf) == 0:
        dim_list.append(dim)
        if check_rf0_group(rf, 0, 10):
            stable_dim_list.append(dim)

c = collections.Counter(rf_count)

bins = np.arange(0, 354, 10) 
plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.hist(sum_aminoindex, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('アミノ酸指標の数')
plt.ylabel('次元数')


print("最小RF距離カウント:", c)
print(dim_list)
print("安定RF距離カウント:",len(stable_dim_list))
print(stable_dim_list)
print("安定アミノ酸指標数")
print(sum_aminoindex, sum(sum_aminoindex))
pd.DataFrame(list(zip(stable_dim_list, sum_aminoindex))).to_csv("../data/histgram.csv", header=False, index=False)

plt.savefig("../image/sum_used_aaindex.png", format="png")
plt.show()