import networkx as nx
import node_mappings

node_descriptions = node_mappings.getNodeMappings() # key: node ID (int), value: node description (string)
print(node_descriptions)

DG = node_mappings.getDigraph()

current_node = 0

while len(list(DG.successors(current_node))) > 0:
    # If the only successor is a capability, recommend that capability to the user
    if len(list(DG.successors(current_node))) == 1 and node_descriptions[list(DG.successors(current_node))[0]][0:4] == 'CAP_':
        current_node = list(DG.successors(current_node))[0]
        break

    # Otherwise, give the user options to choose from
    print('Please choose the number corresponding to the option that is most relevant to what you are trying to configure.')
    print("Options: ")
    options = [node_descriptions[successor] for successor in list(DG.successors(current_node))] # list of [description, node ID]
    for option in options:
        print(str(options.index(option)) + ': ' + option)
    user_choice = input()

    # Check if input is valid. If not, stay at the current node and present the options to the user again.
    try:
        user_choice = int(user_choice)
    except:
        print("Please select one of the options provided.")
        continue
    if user_choice >= len(options):
        print("Please select one of the options provided.")
        continue

    # If input is valid, move down the tree by moving to a more specific option
    next_node = list(DG.successors(current_node))[user_choice]
    current_node = next_node

# Leaf (capability) has been reached
print('Recommended Capability: ' + str(node_descriptions[current_node]))


