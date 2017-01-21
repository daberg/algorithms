class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            new = Node(data)

            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = new

    def dequeue(self):

        if self.head is None:
            return None

        temp = self.head.data
        self.head = self.head.next

        return temp

    def is_empty(self):
        return self.head is None

    def top(self):

        if self.head is None:
            return None

        return self.head.data


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(8)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.top())
    print(queue.dequeue())
