"""
Linked List Nth to Last Node
Problem Statement
Write a function that takes a head node and an integer value n and then returns the nth to last node value in the linked list.
"""

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    right_pointer, left_pointer = head, head

    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    return left_pointer.value

# Testing
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(nth_to_last_node(2,a))
