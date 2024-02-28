# in anaconda prompt use command "conda install conda-forge::binarytree" to get the binarytree module

from binarytree import build

nodes = [1, 11, 3, 33, 4, 44]

binary_tree = build(nodes)
print(binary_tree)
