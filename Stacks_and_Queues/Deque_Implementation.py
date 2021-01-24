
"""
Deque Implementation:

Major Difference between Queue and Deque is we can add items at either
front or rear and also removal of items can be wither done at front or rear.

Methods:
    Deque() - Creates a new deque that is empty
    addFront(item)
    addRear(item)
    removeFront(item)
    removeRear(item)
    isEmpty()
    size()
"""

class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def removeFront(self):
        return self.items.pop()

    def display(self):
        return " ".join(map(str, list(self.items)))


d = Deque()

d.addFront('1')
d.addRear('2')
d.addRear('3')
d.addFront('4')
print("Deque: ",d.display())
print("Size of Deque: ", d.size())
print("Remove Front: ",d.removeFront())
print("Deque: ",d.display())
print("Remove Front: ",d.removeFront())
print("Deque:",d.display())
print("Remove Rear: ",d.removeRear())
print("Deque:",d.display())
print("Size of Deque: ", d.size())
print("Remove Rear: ",d.removeRear())
print("Deque: ",d.display())
print("Size of Deque: ", d.size())

