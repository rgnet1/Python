#!/usr/bin/python3
# Ramzey Ghanaim
# Dijkstra's Algorithm


 #  Dikjstra's algorithm:
def myDijkstra(my_graph):
    # List of all vertecies
    L = my_graph['vertecies']

    # List of disances, pre-populated with "infinity"
    D = [float('inf')] * len(my_graph['vertecies'])

    # Fill List of paths with "None" (same thing as NULL)
    T = [None] * len(my_graph['vertecies'])
    
    # Start source node at 1
    source_node = 1
    edges = list(my_graph['edges'])

    print("----------------BEGIN-----------------")
    print("L:", L)
    print("D:", D)
    print("T:", T)
    print("--------------------------------------")

    D[source_node-1] = 0
    min_selector = 0
    while len(L) >1:
        print("================Itteration:",source_node,"===================")
        print("Source Node: ", source_node)
        
        # Itterate thorugh edges
        for one_edge in edges:
            
            # extract edge properties from edge data type
            weight, v1, v2 = one_edge
            if v1 == source_node:
                if D[v2-1] > D[v1-1] + weight:
                    D[v2-1] = D[v1-1] + weight
                    T[v2-1] = v1
                elif weight < D[v2-1]:
                    D[v2-1] = weight
                    T[v2-1] = T[v2-1] +1          
        L.remove(source_node)

        #                       Select Next Vertex
        # Determine NEXT SOURCE NODE based on previously selected minimum value in D
        tmp_min = min(x for x in D if x > min_selector )
        source_node = D.index(tmp_min)+1
        min_selector = tmp_min
    
        # Print output
        print("D: ", D)
        print("T:", T)
        print("L:", L)
    print("Algorithm finished")


# Add graph as a python dictionary of vertecies and edges
#       class example graph formatted using python dictionaries
class_example = {
    'vertecies': [1, 2, 3, 4, 5, 6],
    
    # edge format: (weight, v_i, v_j)
    #  v_i = v1,  v_j = v2
    'edges': set(
        [
            (3, 1, 2),
            (5, 1, 3),
            (1, 2, 3),
            (2, 2, 4),
            (6, 3, 4),
            (2, 3, 5),
            (5, 4, 6),
            (7, 5, 3),
            (3, 5, 4),
            (1, 5, 6),
            (4, 6, 4),
        ]
    )
}

#       assn1 graph
hw = {
    'vertecies': [1, 2, 3, 4, 5, 6],
    
    # edge format: (weight, v_i, v_j)
    #  v_i = v1,  v_j = v2
    'edges': set(
        [
            (1, 1, 2),
            (2, 1, 3),
            (5, 2, 3),
            (7, 2, 4),
            (1, 3, 4),
            (2, 3, 5),
            (2, 4, 6),
            (8, 5, 3),
            (3, 5, 4),
            (5, 5, 6),
            (9, 6, 4),
        ]
    )
}

# Run algorithm with specified graph
myDijkstra(hw)

