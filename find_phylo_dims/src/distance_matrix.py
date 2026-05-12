import numpy as np
import pandas as pd
import math
from scipy.spatial.distance import pdist, squareform

id_list = np.array(pd.read_csv("../data/ND5_9.csv", header=None))[:, 0]

def Distance_Matrix(vec, id_list):
    def Cos_Similarity(v1, v2):
        if np.array_equal(v1, v2):
            return 0.0
        
        cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos = np.clip(cos, -1.0, 1.0)
        theta = math.acos(cos)
        return theta

    def Euclidean_Distance(vec):
        dist_vector = pdist(vec, metric='euclidean')  
        dist_matrix = squareform(dist_vector)
        return dist_matrix.tolist()

    DM_cos = [[0] * len(id_list) for _ in range(len(id_list))]
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            DM_cos[i][j] = Cos_Similarity(vec[i], vec[j])
            DM_cos[j][i] = DM_cos[i][j]


    DM_euclid = Euclidean_Distance(vec)

    return np.array(DM_cos), np.array(DM_euclid)

        



