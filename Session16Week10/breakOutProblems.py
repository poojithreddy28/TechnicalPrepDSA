from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def is_balanced(display):
    # def check_balanced(node,h1,h2):
    #     if h1-h2>1:
    #         return False
    #     if node is None:
    #         return True
    #     return check_balanced(node.left,h1+1,h2) and check_balanced(node.right,h1,h2+1)
    if not display:
        return True
    # def get_height(node):
    #     if node is None:
    #         return 0
    #     return 1+ max(get_height(node.left),get_height(node.right))
    # if abs(get_height(display.left)-get_height(display.right))>1:
    #     return False
    # return is_balanced(display.left) and is_balanced(display.right)

def is_balanced(root):
    def check(node):
        if node is None:
            return 0  # height = 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1

# Example Usage:

"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"]
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  
#        🍰
#      /     \
#    🍩       🥧
#   /  \     /  \
# 🧁  🥐   🥖  🍪
baked_goods = ["🍰", "🍩", "🥧", "🧁", "🥐", "🥖", "🍪"]
display = build_tree(baked_goods)
print(is_balanced(display))  # True
#     🥞
#       \
#        🍮
#          \
#           🍪
baked_goods = ["🥞", None, "🍮", None, "🍪"]
display = build_tree(baked_goods)
print(is_balanced(display))  # False
# Example Output:

# True
# False