class Queue:
    def __init__(self, queue_1):
        self.items = []
        self.queue_1 = queue_1

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def queue_to_stack(self):
        self.queue_1.reverse()
        for items in self.queue_1:
            self.items.append(items)
        return self.items

    
print(Queue([5, 4, 3, 2, 1]).queue_to_stack())
