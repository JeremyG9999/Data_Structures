class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data
    def is_empty(self):
        return self.top is None
    def printStack(self):
        temp = self.top
        while (temp):  
            print(temp.data)
            temp = temp.next
def main():
    stacks = Stack()
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    stacks.pop()
    print("\nStack:")
    stacks.printStack()
    print("\nStack Peek at Top:")
    print(stacks.peek())