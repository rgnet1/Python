#!/usr/bin/python3
# Ramzey Ghanaim
# MST Algorithm - Kruzkal



# Add graph as a python dictionary of verteciesand edges
my_graph = {
    'vertecies': [1, 2, 3, 4, 5,],
    'edges': set(
        [
            (3, 1, 2),
            (4, 1, 3),
            (5, 1, 4),
            (6, 1, 5),
            (1, 2, 3),
            (4, 2, 4),
            (2, 2, 5),
            (5, 3, 4),
            (7, 3, 5),
            (3, 4, 5),
        ]

    )
}

# Keep ranks and parents as dicitonaries
rank = dict()
parent = dict()


#      make_set()
#
# @param: verticy - single vertecy
#
# This fucntion creates a new set of a single verticy
#
def make_set(verticy):
    # Assign new node to it's own parent (rooot)
    parent[verticy] = verticy
    rank[verticy] = 0


#          find_set()
#
# @param: vertecy - single vertecy
#
# This function finds the root of specified vertecy
#
def find_set(vertecy):
    if parent[vertecy] != vertecy:
        parent[vertecy] = find_set(parent[vertecy])

    return parent[vertecy]

#        link_roots()
#
# @param: vertecy1 - first verticy you want to merge
# @param: vertecy2 - second verticy you want to merge
#
# combine two disjoing sets based on 2 provided vertcies.
# This funciton finds the roots, using find_set and then
# continues to merge the roots together
#
def link_roots(vertecy1, vertecy2):
    R1 = find_set(vertecy1)
    R2 = find_set(vertecy2)
    if R1 == R2:
        return
    if rank[vertecy1] > rank[vertecy2]:
        parent[R2] = R1
    else:
        parent[R1] = R2

    if rank[R2] == rank[R1]:
        rank[R2] += 1


#          get_tree_cost()
#
# @param - tree - final mst tree to calculate total cost of
#
# @return - sum - sum of all edge costs in tree
def get_tree_cost(tree):
    sum = 0
    for edge in tree:
        weight, v1, v2 = edge
        sum+=weight
    return sum
#            main()
#
# @param - my_graph - graph with specified edges, weights, and verteceis
#
# @return - final_result - final MST found by using Kruzkal and disjoint sets
#
# This driver function creates a Minimum spanning tree using Kruzal's algorithm
# and disjoing sets
def main(my_graph):

    # Sort vertecies/edges, and make individual sets:
    for verticy in my_graph['vertecies']:
        make_set(verticy)
        mst = set()
    edges = list(my_graph['edges'])
    edges.sort()

    # Create MST
    for one_edge in edges:
        # extract weights and vertecies from edge
        weight, v1, v2 = one_edge
        if find_set(v1) != find_set(v2):
            link_roots(v1, v2)
            mst.add(one_edge)

    final_result = sorted(mst)
    tree_cost = get_tree_cost(final_result)
    return final_result, tree_cost


# Driver code to demonstrate:
print("Initial Graph:")
print("         ", my_graph)
print("\n\nFinal Result:")
mst, cost = main(my_graph)
print("         ",mst )
print("Cost of tree is", cost)