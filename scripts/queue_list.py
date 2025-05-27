class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def dequeue(self):
        if self.head is None:
            return None  
        else:
            tempnode = self.head
            self.head = tempnode.next
            return tempnode.data
    def enqueue(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
        return newnode.data
    def is_empty(self):
        return self.head is None
    def printList(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print(elements)
def main():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue(7)
    queue.enqueue(6)
    queue.dequeue()
    print("Queue:")
    queue.printList()