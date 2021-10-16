class Queue:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.size() > 0:
            return self.items.pop(0)
        return None
    
    def peek(self):
        if self.size() > 0:
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    def print(self):
        print("Contents of Queue(Right is open) are: ")
        for i in self.items:
            print(i, end=' ')
        print()

if __name__=='__main__':
    queue = Queue()
    queue.push(2)
    queue.push(5)
    queue.push(4)
    queue.print()
    print("Peeked element: " + str(queue.peek()))
    print("Popped element: " + str(queue.pop()))
    print("Popped element: " + str(queue.pop()))
    queue.print()
