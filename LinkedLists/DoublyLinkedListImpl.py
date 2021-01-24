"""

"""

class Node(object):

    def __init__(self,value):

        self.value = value
        self.next = None
        self.prev = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
b.prev = a
c.prev = b

print(a.value)
print(a.next.value)
print(b.value)
print(b.next.value)
print(b.prev.value)
