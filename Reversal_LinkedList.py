"""
Linked List Reversal
Problem
Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and return the new head of the list.
and Function operates in O(1)
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

"""
Store the current next node value to temporary value next
Update the current next node value to previous value prev
Update previous to current
Update current to next
"""

def reversal(node):
    cur = node
    prev, nxt = None, None
    while cur:
        nxt = cur.nextnode
        cur.nextnode = prev
        prev = cur
        cur = nxt
    return prev


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

reversal(a)

print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)
