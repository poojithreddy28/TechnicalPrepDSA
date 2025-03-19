class dog:
    def __init__(self,name,color):
        self.name = name 
        self.color = color
    def bark(self):
        print("{} is barking".format(self.name))
obj1 = dog("Ruby","Brown")
obj2 = dog("Max","Black")
# print("My dog name is {} and its color is {}".format(obj1.name,obj1.color))
# obj1.bark()
# print("My dog name is {} and its color is {}".format(obj2.name,obj2.color))
# obj2.bark()



class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

dog_node1= Node("Ruby")
dog_node2 = Node("Max")
dog_node1.next = dog_node2
print("dog_node1 value is {} and dog_node2 pointer is {}".format(dog_node1.value,dog_node1.next))
print("dog_node2 value is {} and dog_node2 pointer is {}".format(dog_node2.value,dog_node2.next))


# TC  =  O(n)[n is the number of elements in the linked list], and SC = O(1)[We are storing just the pointer to the next node] 
# Insertion at the end of the linked list is O(1) operation


class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
