import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import distance_matrix
import make_tree

id_list = np.array(pd.read_csv("../data/ND5_9.csv", header=None))[:, 0]
dims = range(0, 2560) # 使用plmが2560次元のため
aaindex_mean = pd.read_csv("../aaindex/data/vec/mean.csv", index_col=0)
newick_clustalo = np.array(pd.read_csv("../clustalo/clustaltree.csv", header=None))[0, 0]

for dim in tqdm(dims, desc="no.1"):
    corr_aaindex = pd.read_csv(f"../data/corr_aaindex/corr_aaindex_{dim}.csv", index_col=0, header=None)

    rf_list = np.zeros(354) # 本研究で使用するアミノ酸指標が354個のため
    for i in tqdm(range(354), desc="no.2", leave=False): # 本研究で使用するアミノ酸指標が354個のため
        index = list(corr_aaindex.iloc[:i].index)

        feature = np.array(aaindex_mean.loc[index])

        DM_cos, DM_euclid = distance_matrix.Distance_Matrix(feature.T, id_list)
        tree_data = {
                    "cos_nj" : make_tree.NJ(DM_cos, "cos_nj", id_list),
                    "cos_upgma" : make_tree.UPGMA(DM_cos, "cos_upgma", id_list),
                    "euclid_nj" : make_tree.NJ(DM_euclid, "euclid_nj", id_list),
                    "euclid_upgma" : make_tree.UPGMA(DM_euclid, "euclid_upgma", id_list)
        }
        rf_list[i] = min(make_tree.eval(tree_data, newick_clustalo))

    pd.DataFrame(rf_list).to_csv(f"../data/RF_aaindex/RF_aaindex_{dim}.csv", header=False, index=False)
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
    plt.plot(range(354), rf_list) # 本研究で使用するアミノ酸指標が354個のため
    # plt.title(f"{dim+1}次元アミノ酸指標でのRF距離")
    plt.xlabel("アミノ酸指標の数")
    plt.ylabel("最小RF距離")
    plt.ylim(0, 12) # 生物種が9種の場合最大RF距離は12となる
    plt.savefig(f"../image/RF_aaindex/RF_aaindex_{dim}.png", format="png")
    plt.clf()