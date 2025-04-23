# # class GraphNode:

# #   def __init__(self, value, edges = None)
# #       self.val = value
# #       if not edges:
# #           self.edges = []
# #       else:
# #           self.edges = edges

# #   def add_connection(self, new_node):
# #       self.edges.append(new_node)

# """
# JFK ----- LAX
# |
# |
# DFW ----- ATL
# """
# # No starter code is provided for this problem
# # Add your code here
# # Example Usage:
# class GraphNode:

#   def __init__(self, value, edges = None):
#       self.val = value
#       if not edges:
#           self.edges = []
#       else:
#           self.edges = edges

#   def add_connection(self, new_node):
#       self.edges.append(new_node)

# flights = {
#     'JFK': ['LAX', 'DFW'],
#     'LAX': ['JFK'],
#     'DFW': ['ATL','JFk'],
#     'ATL': ['DFW']     
# }
# for flight in flights.keys():
#     graph = GraphNode(flight)
#     graph.add_connection(flights[flight])
#     print(graph.val, graph.edges)

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])
# # Example Output:

# # ['JFK', 'LAX', 'DFW', 'ATL']
# # [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
# # ['LAX', 'DFW']


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))