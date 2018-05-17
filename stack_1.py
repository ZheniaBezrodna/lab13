class Stack:
    def __init__(self, stack_1):
        self.items = []
        self.stack_1 = stack_1

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def stack_to_queue(self):
        self.stack_1.reverse()
        for items in self.stack_1:
            self.items.append(items)
        return self.items


print(Stack([1, 2, 3, 4, 5]).stack_to_queue())