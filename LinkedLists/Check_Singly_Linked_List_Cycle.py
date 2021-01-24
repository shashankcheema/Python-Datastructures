"""
Problem:
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
"""

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextNode != None:

        marker1 = marker1.nextNode
        marker2 = marker2.nextNode.nextNode

        if marker2 == marker1:
            return True
    return False

# Cycle Linked List
a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = a

print(cycle_check(a))

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(x))
