from stack import Stack
from queue import Queue


class Node:

    def __init__(self, key, data=None):

        self.key = key
        self.data = data
        self.left = None
        self.right = None


def print_node(node):
    print(str(node.key) + " --> " + str(node.data))


class BinarySearchTree:

    def __init__(self):

        self.root = None

    def add(self, key, data=None):

        if self.root is None:
            self.root = Node(key, data)

        else:
            self._add(self.root, key, data)

    def _add(self, node, key, data):

        if node.key == key:
            return None

        elif key < node.key:

            if node.left is None:
                node.left = Node(key, data)

            else:
                self._add(node.left, key, data)

        else:

            if node.right is None:
                node.right = Node(key, data)

            else:
                self._add(node.right, key, data)

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
            left_count = self._tail_rec_count(node.left, count)
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

    def iter_preorder_visit(self, on_visit):

        if self.root is None:
            print("Tree is empty.")

        else:
            nstack = Stack()
            nstack.push(self.root)

            while not nstack.is_empty():
                curr = nstack.pop()

                if curr is not None:
                    on_visit(curr)
                    nstack.push(curr.right)
                    nstack.push(curr.left)

    def preorder_visit(self, on_visit):

        self._preorder_visit(self.root, on_visit)

    def _preorder_visit(self, node, on_visit):

        if node is not None:
            on_visit(node)
            self._preorder_visit(node.left, on_visit)
            self._preorder_visit(node.right, on_visit)

    def postorder_visit(self, on_visit):

        self._postorder_visit(self.root, on_visit)

    def _postorder_visit(self, node, on_visit):

        if node is not None:
            self._postorder_visit(node.left, on_visit)
            self._postorder_visit(node.right, on_visit)
            on_visit(node)

    def inorder_visit(self, on_visit):

        self._inorder_visit(self.root, on_visit)

    def _inorder_visit(self, node, on_visit):

        if node is not None:
            self._inorder_visit(node.left, on_visit)
            on_visit(node)
            self._inorder_visit(node.right, on_visit)

    def preorder_print(self):

        if self.root is None:
            print("Empty tree.")

        else:
            self.preorder_visit(print_node)

    def postorder_print(self):

        if self.root is None:
            print("Empty tree.")

        else:
            self.postorder_visit(print_node)

    def inorder_print(self):

        if self.root is None:
            print("Empty tree.")

        else:
            self.inorder_visit(print_node)

    def breadth_first_visit(self, on_visit):

        if self.root is not None:

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

    def has(self, key):

        return self._has(self.root, key)

    def _has(self, node, key):

        if node is None:
            return False

        elif node.key == key:
            return True

        else:
            return self._has(node.left, key) or self._has(node.right, key)
    
    def get(self, key):
        
        return self._get(self.root, key)

    def _get(self, node, key):

        if node is None:
            return None

        if node.key == key:
            return node.data

        elif node.key < key:
            return self._get(node.right, key)

        else:
            return self._get(node.left, key)

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

    def min_node(self):

        if self.root is None:
            return None

        else:
            return self._min_node(self.root)

    def _min_node(self, node):

        if node.left is None:
            return node

        else:
            return self._min_node(node.left)

    def max_node(self):

        if self.root is None:
            return None

        else:
            return self._max_node(self.root)

    def _max_node(self, node):

        if node.right is None:
            return node

        else:
            return self._max_node(node.right)

    def remove(self, key):

        if self.root is None:
            return None

        else:
            return self._remove(self.root, key, None)
    
    def _remove(self, node, key, parent):

        if node is None:
            return None

        else:

            if node.key == key:

                if node.left is None and node.right is None:

                    if parent is not None:

                        if parent.left is node:
                            parent.left = None

                        elif parent.right is node:
                            parent.right = None

                    else:
                        self.root = None
                        
                    return node.data

                if node.left is not None and node.right is not None:
                    
                    prev = node
                    curr = node.right

                    while curr.left is not None:
                        prev = curr
                        curr = curr.left

                    successor = curr

                    successor.left = node.left
                    successor.right = node.right.right

                    # Do this after the = node.left assignment because
                    # prev could be node itself
                    prev.left = None

                    if parent is not None:

                        if parent.left is node:
                            parent.left = successor

                        elif parent.right is node:
                            parent.right = successor

                    else:
                        self.root = successor
                            
                    return node.data

                if node.left is not None:

                    if parent is not None:

                        if parent.left is node:
                            parent.left = node.left

                        elif parent.right is node:
                            parent.right = node.left

                    else:
                        self.root = node.left

                    return node.data

                if node.right is not None:

                    if parent is not None:

                        if parent.left is node:
                            parent.left = node.right

                        elif parent.right is node:
                            parent.right = node.right

                    else:
                        self.root = node.right

                    return node.data

            elif node.key < key:
                return self._remove(node.right, key, node)

            else: # node.key > key
                return self._remove(node.left, key, node)
                            

tree = BinarySearchTree()
tree.add(10, 214)
tree.add(14, 123)
tree.add(235, 7)
tree.add(9, "test")
tree.add(27, Queue())
tree.add(98, "lol")
tree.add(126)
tree.inorder_print()
print()
tree.remove(10)
tree.inorder_print()
print()
tree.remove(126)
tree.inorder_print()
print()
tree.remove(9)
tree.inorder_print()
print()
tree.remove(98)
tree.inorder_print()
print()
tree.remove(235)
tree.inorder_print()
print()
tree.remove(14)
tree.inorder_print()
print()
tree.remove(27)
tree.inorder_print()
print()
