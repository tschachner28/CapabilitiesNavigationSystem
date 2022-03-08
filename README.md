# CapabilitiesNavigationSystem

## Description
This tool serves to help users find the Linux capabilities that suit their needs. 
In this tool, categories are presented to the user, and the user enters the number corresponding to the category that 
is most relevant for their purposes. The user then selects more and more specific categories until a capability is reached, 
which is then recommended to the user.

## Using the Tool
1. Clone this github repo.
2. Navigate to this repo's directory in your filesystem and run the following command: pip install -r requirements.txt
3. Run main.py and follow the prompts, entering the number corresponding to the option that is most relevant to the capabilities you need. 
If you find that more than one option is relevant, choose one for now, and then rerun main.py later, selecting the other option.
You will eventually be presented with a recommended capability each time you run the tool.

## Code Description
### Tree Structure
#### getDigraph()
The categories and capabilities are stored in the DiGraph object DG, which is created using the networkx package.
This DiGraph object, which contains a list of directed edges from the node ID of one node to another 
(as shown in this diagram: https://app.diagrams.net/?title=(Labeled)%20Capabilities%20Navigation%20System.drawio&client=1#G1l3VgVhNALkmFLHG9lg2QLnGnXiwd27n8), 
can be obtained using the function getDigraph() in node_mappings.py. 

#### getNodeMappings()
The getNodeMappings() function in node_mappings.py returns a dictionary in which each key is a node ID and each value is 
the text in that node, as shown in the diagram linked above. This text either corresponds to a category or a capability.
These mappings are used to show the categories and capabilities to the user so they can provide the input needed for navigating through the tree.

### Main Script
main.py navigates through the DiGraph object based on user input. It keeps track of current_node, which is initialized to 
the root (node 0) and is then updated each time the user selects an option. 

main.py contains a while loop that terminates when a capability (leaf) is reached. If a capability has not yet been reached,
the options branching out from current_node are presented to the user. Each option is assigned a number that corresponds to its index in the list of current_node's successors. 
The user selects a category by entering the number corresponding to the most relevant option. When a capability is reached,
that capability is printed and recommended to the user.