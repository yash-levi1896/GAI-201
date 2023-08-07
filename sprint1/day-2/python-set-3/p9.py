from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue2.put(value)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if not self.queue1.empty():
            return self.queue1.get()
        return None

# Test case
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.pop())  
stack.push(3)
print(stack.pop())  
print(stack.pop())  
print(stack.pop())  
