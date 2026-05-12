import torch
import esm
import pandas as pd
import numpy as np
import tqdm


# モデルの読み込み
model, alphabet = esm.pretrained.esm2_t36_3B_UR50D()
batch_converter = alphabet.get_batch_converter()
model = model.eval()


def get_emb(data):
    batch_labels, batch_strs, batch_tokens = batch_converter(data)
    
    with torch.no_grad():
        results = model(
            batch_tokens, 
            repr_layers=[36], # モデル最終層(36層)から取得
            return_contacts=False
        )

    rep = results["representations"][36] # モデル最終層(36層)から取得

    for i, name in enumerate(batch_labels):
        length = len(batch_strs[i])

        emb = rep[i, 1:length+1]
        print(len(emb))

        pd.DataFrame(emb, dtype=float).to_csv(
            f"../data/{name}_vec.csv", 
            header=False, 
            index=False
        )


        




nd5_9 = np.array(pd.read_csv(f"../data/ND5_9.csv", header=None))

for amino_seq in nd5_9:
    get_emb([amino_seq])

# get_emb(graph9)
