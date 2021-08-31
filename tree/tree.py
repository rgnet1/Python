
tree = {

    # format: Node: [Parent, Left Child, Right Child]

    50: [None, 48, 51],
    51: [50, None, None],
    48: [50, 32, 49],
    49: [48, None, None],
    32: [48, 15, 36],
    15: [32, 10, 20],
    36: [32, None, 49],
    10: [15, 11, 4],
    20: [15, 16, 21],
    47: [36, None, None],
    11: [10, None, None],
    4: [10, None, None],
    16:[20, None, None],
    21: [20, None, None],

}


def searchAndClean(tree):
    root = 50
    current_node = 50
    while tree[current_node][1] is not None:
        # find leftmost
        print("Looking at Node: ", tree[current_node][1])
        current_node = tree[current_node][1]
    parent = -1
    while parent != root:
        parent = tree[current_node][0]
        if tree[parent][1] > parent:
            tree.pop(current_node)
        current_node = tree[parent][2]
        if tree[parent][2] < parent:
            tree.pop(current_node)
        current_node = tree[parent]
    
    return tree

print(searchAndClean(tree))
