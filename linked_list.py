class Iterator:
    
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def __iter__(self):
        return self

    def __next__(self):
        pass


class Node:

    def __init__(self, data=None):
        
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def __iter__(self):

        curr = self.head

        while curr:
            yield curr.data
            curr = curr.next

    def push(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

        else:

            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.head is not None:
            self.head = self.head.next

    def as_last(self, data):

        new_node = Node()
        new_node.data = data

        if self.head is None:

            self.head = new_node

        else:

            iterator = self.head

            while iterator.next is not None:

                iterator = iterator.next

            iterator.next = new_node

    def reverse(self):

        if self.head is None:
            return

        prev = None
        curr = self.head

        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = curr
        self.head.next = prev

    def search(self, data):

        iterator = self.head

        while iterator is not None:

            if iterator.data == data:
                return True

            iterator = iterator.next

        return False

    def count(self):

        if self.head is None:
            return 0

        else:
            
            count = 0
            curr = self.head

            while curr is not None:
                count = count + 1
                curr = curr.next

            return count

    def print(self):

        if self.head is None:
            print("Empty list")

        else:

            iterator = self.head

            output = ""

            while iterator is not None:
                output = output + str(iterator.data) + " "
                iterator = iterator.next

            print(output)

"""
llist = LinkedList()
llist.push(3)
llist.push(5)
llist.push(1)
llist.as_last(12)
for element in llist:
    print(element)
"""
