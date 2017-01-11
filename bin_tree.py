from stack import Stack
from queue import Queue

class Node:

    def __init__(self, data=None):
        
        self.data  = data
        self.left  = None
        self.right = None

def print_node(node):
    print(node.data)

class BinaryTree:

    def __init__(self):

        self.root = None

    def add(self, data):

        if self.root is None:
            self.root = Node(data)

        else:
            self._add(self.root, data)

    def _add(self, node, data):

        if node.data == data:
            return None

        elif data < node.data:
            
            if node.left is None:
                node.left = Node(data)

            else:
                self._add(node.left, data)

        else:

            if node.right is None:
                node.right = Node(data)

            else:
                self._add(node.right, data)

    def count(self):
        return self._count(self.root)

    def _count(self, node):

        if node is None:
            return 0

        else:
            return 1 + self._count(node.left) + self._count(node.right)

    def tail_rec_count(self):
        return self._tail_rec_count(self.root, 0)

    def _tail_rec_count(self, node, count):

        if node is None:
            return count

        else:
            # The left call actually makes this not tail recursive :(
            left_count =  self._tail_rec_count(node.left, count) 
            return self._tail_rec_count(node.right, left_count + 1)

    def height(self):

        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        else:
            left_h = self._height(node.left)
            right_h = self._height(node.right)

            return left_h + 1 if left_h > right_h else right_h + 1

    def print(self):

        if self.root is None:
            print("Tree is empty.")

        else:
            self._print(self.root)

    def _print(self, node):

        if node is not None:
            self._print(node.left)
            print(node.data)
            self._print(node.right)

    def iter_preorder_print(self):

        if self.root is None:
            print("Tree is empty.")

        else:
            nstack = Stack()
            nstack.push(self.root)

            while not nstack.is_empty():
                curr = nstack.pop()
                
                if curr is not None:
                    print(curr.data)
                    nstack.push(curr.right)
                    nstack.push(curr.left)

    def breadth_first_visit(self, on_visit):

        if self.root is None:
            print("Tree is empty.")

        else:
            nqueue = Queue()
            nqueue.enqueue(self.root)

            while not nqueue.is_empty():
                curr = nqueue.dequeue()

                if curr is not None:
                    on_visit(curr)
                    nqueue.enqueue(curr.left)
                    nqueue.enqueue(curr.right)

    def breadth_first_print(self):

        self.breadth_first_visit(print_node)
    
    def has(self, data):

        return self._has(self.root, data)

    def _has(self, node, data):

        if node is None:
            return False

        elif node.data == data:
            return True

        else:
            return self._has(node.left, data) or self._has(node.right, data)

    def count_leaves(self):

        if self.root is None:
            return 0

        else:
            return self._count_leaves(self.root)

    def _count_leaves(self, node):

        if node is None:
            return 0

        elif node.left is None and node.right is None:
            return 1

        else:
            return (self._count_leaves(node.left)
                    + self._count_leaves(node.right))


tree = BinaryTree()
tree.add(10)
tree.add(14)
tree.add(235)
tree.add(9)
tree.add(27)
tree.add(98)
tree.add(126)
print(tree.count_leaves())

