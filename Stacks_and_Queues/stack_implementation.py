"""
Stack Implementation in Python

"""

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        # Checking is Stack is Empty
        return self.items == []

    def push(self, item):
        # Appending an element to the Stack
        self.items.append(item)

    def pop(self):
        # Remove the last element
        return self.items.pop()

    def peek(self):
        # return the last element from the stack
        return self.items[len(self.items)-1]

    def size(self):
        # Return Size of the stack
        return len(self.items)

s = Stack()
print("Is Stack Empty:",s.isEmpty())
s.push('one')
s.push('two')
print("Is Stack Empty:",s.isEmpty())
print("Size of Stack:", s.size())
print("Last Element:", s.peek())
s.pop()
print("Size of Stack:", s.size())
print("Last Element:", s.peek())
s.pop()
print("Size of Stack:", s.size())
print("Is Stack Empty:",s.isEmpty())