# coding: utf-8

from anytree import Node, RenderTree

data = """
ANIMAL
#MAMMAL
##CARNIVORA
    DOG
    CAT
##PRIMATES
    MONKEY
    HUMAN
#BIRD
##PASSERIFORMES
    SPARROW
    SWALLOW
#AQUATIC
    SALMON
    TUNA
PLANT
#FLOWERING
    ROSE
    ORCHID
    TULIP
#NONFLOWERING
    FERN
    MOSS
"""

# dataを解析してツリーを作成
# "#"がdepth 1, "##"がdepth 2, "    "がdepth 3を表す
root = Node("root", depth=-1)
parent = root
for line in data.splitlines():
    if not line.strip():
        continue

    if line.startswith("    "):
        depth = 3
    elif line.startswith("##"):
        depth = 2
    elif line.startswith("#"):
        depth = 1
    else:
        depth = 0

    name = line.lstrip("# ")

    # fixme: ツリー構造がおかしい
    while parent.depth < depth:
        if isinstance(parent.parent, Node):
            parent = parent.parent

    print(f"depth: {depth}, name: {name}, parent: {parent.name}")
    parent = Node(name, parent=parent, depth=depth)


# ツリーを表示
for pre, fill, node in RenderTree(root):
    print("%s%s (%d)" % (pre, node.name, node.depth))
