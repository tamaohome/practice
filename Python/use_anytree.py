# coding: utf-8

from anytree import Node, RenderTree


data = """
#ANIMAL
##MAMMAL
###CARNIVORA
    DOG
    CAT
###PRIMATES
    MONKEY
    HUMAN
##BIRD
###PASSERIFORMES
    SPARROW
    SWALLOW
##AQUATIC
    SALMON
    TUNA

#PLANT
##FUNGUS
##FLOWERING
    ROSE
    ORCHID
    TULIP
##NONFLOWERING
    FERN
    MOSS
"""


def line_depth(line):
    if "#" in line:
        return line.count("#")
    else:
        return -1


def set_tree(lines: list[str]) -> Node:
    root = Node("root")
    parent = root

    for line in lines:
        if not line.strip():
            continue

        depth = line_depth(line)
        name = line.lstrip("# ")

        if depth < 0:
            Node(name, parent=parent)
        elif depth > parent.depth:
            parent = Node(name, parent=parent)
        elif depth == parent.depth:
            parent = Node(name, parent=parent.parent)
        else:
            while depth <= parent.depth:
                if isinstance(parent.parent, Node):
                    parent = parent.parent
            parent = Node(name, parent=parent)

    return root


def display_tree(root):
    for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


if __name__ == "__main__":
    lines = [line.strip("\n") for line in data.split("\n")]
    root = set_tree(lines)
    display_tree(root)


"""
-> 以下のようにツリーが表示される

root
├── ANIMAL
│   ├── MAMMAL
│   │   ├── CARNIVORA
│   │   │   ├── DOG
│   │   │   └── CAT
│   │   └── PRIMATES
│   │       ├── MONKEY
│   │       └── HUMAN
│   ├── BIRD
│   │   └── PASSERIFORMES
│   │       ├── SPARROW
│   │       └── SWALLOW
│   └── AQUATIC
│       ├── SALMON
│       └── TUNA
└── PLANT
    ├── FUNGUS
    ├── FLOWERING
    │   ├── ROSE
    │   ├── ORCHID
    │   └── TULIP
    └── NONFLOWERING
        ├── FERN
        └── MOSS
"""
