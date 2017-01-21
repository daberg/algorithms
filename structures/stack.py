class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            new = Node(data)
            new.next = self.head
            self.head = new

    def pop(self):

        if self.head is None:
            return None

        else:
            tmp = self.head
            self.head = self.head.next
            return tmp.data

    def top(self):

        if self.head is None:
            return None

        return self.head.data

    def is_empty(self):

        return self.head is None


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(7)
    stack.push(8)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
