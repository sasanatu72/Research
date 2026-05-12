import numpy as np 
import pandas as pd 
from skbio import DistanceMatrix
from scipy.cluster.hierarchy import linkage, to_tree
from skbio.tree import nj
from io import StringIO
from ete3 import Tree, TreeStyle
import matplotlib.pyplot as plt
from PIL import Image
import re

id_list = np.array(pd.read_csv("../data/ND5_9.csv", header=None))[:, 0]

def quote_newick_labels(newick):
    pattern = r"([,(])([A-Za-z0-9_]+)(?=[:,)])"
    repl = r"\1'\2'"
    return re.sub(pattern, repl, newick)

def NJ(dm, name, id_list):
    dm = DistanceMatrix(dm, id_list)
    # 系統樹作成
    tree = nj(dm)
    
    tree.unroot() # 根なし
    # tree = tree.root_at_midpoint() # 根あり

    # Newick形式の出力
    output = StringIO()
    tree.write(output, format='newick')
    newick_str = output.getvalue().rstrip("\n")
    
    newick_str = quote_newick_labels(newick_str)

    return newick_str

def UPGMA(dm, name, id_list):
    dm = DistanceMatrix(dm, id_list)
    # condensed form に変換（SciPyの linkage に必要）
    condensed = dm.condensed_form()

    # UPGMA法でクラスタリング（method="average" がUPGMA）
    Z = linkage(condensed, method='average')

    # Newick形式のツリーに変換
    def scipy_to_newick(z, labels):
        """SciPy linkage → Newick形式"""
        tree, nodes = to_tree(z, rd=True)
        def build_newick(node):
            if node.is_leaf():
                return labels[node.id]
            else:
                left = build_newick(node.left)
                right = build_newick(node.right)
                return f"({left}:{node.dist - node.left.dist},{right}:{node.dist - node.right.dist})"
        return build_newick(tree) + ";"

    # Newick文字列を作成
    newick_str = scipy_to_newick(Z, dm.ids)
    
    newick_str = quote_newick_labels(newick_str)

    return newick_str


def eval(newick_list, newick_clustalo):
    t_ref = Tree(newick_clustalo, format=1, quoted_node_names=True)
    t_ref.unroot() # 根なし
    rf_list = []
    for name, newick in newick_list.items():
        t_pred = Tree(newick, format=1, quoted_node_names=True)
        t_pred.unroot() # 根なし
        rf, max_rf = t_ref.robinson_foulds(t_pred, unrooted_trees=True)[:2]
        rf_list.append(rf)
    return rf_list


