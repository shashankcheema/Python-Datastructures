"""
Queue Implementation:
    Queue() - Creates a new Queue that is empty
    enqueue(item) - Adds a new item to the rear of Queue - No return value
    dequeue() - Removes a new item from the front of Queue - No parameters or return value
    isEmpty() - Check to verify Queue is empty
    size() - Return the number of items in Queue
"""

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop()

    def enqueue(self,item):
        self.items.insert(0,item)

q = Queue()
print("Is Queue is Empty:", q.isEmpty())
q.enqueue('one')
q.enqueue('two')
print("Is Queue is Empty:", q.isEmpty())
print("Size of Queue:", q.size())
print("Pop: ", q.dequeue())
print("Pop: ", q.dequeue())
print("Is Queue is Empty:", q.isEmpty())
print("Size of Queue:", q.size())
