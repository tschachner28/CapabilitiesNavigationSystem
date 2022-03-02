import networkx as nx

num_descriptions_mapping = {} # key: node ID (int), value: node description (string)

DG = nx.DiGraph()
DG.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (3, 8), (3, 9), (3, 10), (3, 11), (4, 6), (8, 12), (8, 13), (11, 14), (2, 5), (2, 6), (2, 7), (5, 15), (5, 16), (7, 17), (7, 14)])

#print(list(DG.successors(13)))
#print(list(DG.neighbors(1)))

current_node = 0
while len(list(DG.successors(current_node))) > 0:
    print("Options: ")
    print(list(DG.successors(current_node)))
    next_node = input()

    # Check if input is valid. If not, stay at the current node and present the options to the user again.
    try:
        next_node = int(next_node)
    except:
        print("Please select one of the options provided.")
        continue
    if next_node not in list(DG.successors(current_node)):
        print("Please select one of the options provided.")
        continue

    # If input is valid, move down the tree by moving to a more specific option
    current_node = next_node

# Leaf (capability) has been reached
print(current_node)
#print(list(DG.successors(current_node))[0])


