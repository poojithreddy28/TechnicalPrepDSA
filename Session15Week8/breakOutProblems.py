# from collections import deque 

# # Tree Node class
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)

# root = TreeNode("Trunk")
# print_tree(root)



# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#   if root is None:
#     return 0
#   if root.val =="+":
#      return root.left.val + root.right.val
#   if root.val == "-":
#      return root.left.val - root.right.val
#   if root.val == "*":
#      return root.left.val * root.right.val
#   if root.val== "/":
#      return root.left.val / root.right.val
  
# """
#     +
#   /   \
#  7     5
# """

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))


# Problem 3: Ivy Cutting
# You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#   if root is None:
#     return []
#   return [root.val] + right_vine(root.right)
# # Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))
# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']


# Problem 4: Ivy Cutting II
# If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#   if root is None:
#     return []
#   return [root.val] + right_vine(root.right)
# # Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))
# # Example Output:

# # ['Root', 'Node2', 'Leaf3']
# # ['Root']


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def count_leaves(root):
#     if root is None:
#         return 0
#     if root.left is None and root.right is None:
#         return 1
#     return count_leaves(root.left)+count_leaves(root.right)
# # Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))
# # Example Output:

# # 3
# # 1

# Problem 6: Pruning Plans
# You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned.

# Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def survey_tree(root):
    
# # Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))
# # Example Output:

# ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]


# Problem 7: Foraging Berries
# You've found a wild blueberry bush and want to do some foraging. However, you want to be conscious of the local ecosystem and leave some behind for local wildlife and regeneration. To do so, you plan to only harvest from branches where the number of berries is greater than threshold.

# Given the root of a binary tree representing a berry bush where each node represents the number of berries on a branch of the bush, write a function harvest_berries(), that finds the number of berries you can harvest by returning the sum of all nodes with value greater than threshold.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def harvest_berries(root, threshold):
#   pass
# Example Usage:

# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))
# # Example Output:

# # 38
# # Example 1 Explanation: 
# # - Nodes greater than 6: 8, 10, 20
# # - 8 + 10 + 20 = 38

# # 0
# # Example 2 Explanation: No nodes greater than 30


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_flower(root, flower):
#   if root is None:
#     return False
#   if root.val == flower:
#     return True
#   return find_flower(root.left,flower) or find_flower(root.right,flower)
# Example Usage:

# """
#          Rose
#         /    \
#        /      \
#      Lily     Daisy
#     /    \        \
# Orchid  Lilac    Dahlia
# """

# flower_field = TreeNode("Rose", 
#                         TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
#                                 TreeNode("Daisy", None, TreeNode("Dahlia")))

# print(find_flower(flower_field, "Lilac"))
# print(find_flower(flower_field, "Hibiscus"))
# Example Output:

# True
# False

# Problem 5: Calculating Yield II
# You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

# Leaf nodes have an integer value.
# Non-leaf nodes have a string value of either "+", "-", "*", or "-".
# The yield of a the tree is calculated as follows:

# If the node is a leaf node, the yield is the value of the node.
# Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
# Return the result of evaluating the root node.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass
# Example Usage:

"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(get_decision(apple_tree))
# Example Output:

# 22
# Explanation:
# - 4 - 2 = 2
# - 10 * 2 = 20
# - 2 + 20 = 22