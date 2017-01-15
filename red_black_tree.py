class Node:

    def __init__(self, key, data=None, is_red=True,
                 parent=None, left=None, right=None):

        self.key = key
        self.data = data
        self.red = is_red

        self.parent = parent
        self.left = left
        self.right = right

    def is_red(self):
        return self.red

    def is_black(self):
        return (not self.red)

    def set_red(self):
        self.red = True

    def set_black(self):
        self.red = False

    def set_references(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree():

    def __init__(self):

        self.nil = Node(None, is_red=False)
        self.nil.set_references(self.nil, self.nil, self.nil)
        self.root = self.nil

    def rotate_left(self, node):

        if node.right is self.nil:
            return None

        other = node.right
        node.right = other.left

        if other.left is not self.nil:
            other.left.parent = node

        other.parent = node.parent

        if node.parent is self.nil:
            self.root = other

        elif node is node.parent.left:
            node.parent.left = other

        else:
            node.parent.right = other

        other.left = node
        node.parent = other

    def rotate_right(self, node):

        if node.left is self.nil:
            return None

        other = node.left
        node.left = other.right

        if other.right is not self.nil:
            other.right.parent = node

        other.parent = node.parent

        if node.parent is self.nil:
            self.root = other

        elif node is node.parent.left:
            node.parent.left = other

        else:
            node.parent.right = other

        other.right = node
        node.parent = other

    def add(self, key, data=None):

        parent = self.nil
        curr = self.root

        while curr is not self.nil and curr.key != key:

            parent = curr

            if key < curr.key:
                curr = curr.left

            else: # key > curr.key
                curr = curr.right

        if curr is self.nil:

            node = Node(key, data, True, self.nil, self.nil, self.nil)

            if parent is self.nil:
                self.root = node

            elif key < parent.key:
                parent.left = node
                node.parent = parent

            else: # key > parent.key
                parent.right = node
                node.parent = parent

            self.fix_insert(node)

        else: # curr.key == key

            curr.data = data

    def fix_insert(self, node):
           
        while node is not self.nil:

            parent = node.parent
            gparent = parent.parent
            uncle = gparent.right if gparent.left is parent else gparent.left
            
            # Case: 1
            if parent is self.nil:

                node.set_black()
                self.root = node

                node = self.nil

            # Case: 2
            if parent.is_black():

                node = self.nil

            # Case: 3
            elif uncle.is_red():

                parent.set_black()
                uncle.set_black()
                gparent.set_red()

                node = gparent

            else:

                # Case: 4a
                if parent is gparent.left and node is parent.right:
                    self.rotate_left(parent)
                    node = parent

                # Case: 4b
                elif parent is gparent.right and node is parent.left:
                    self.rotate_right(parent)
                    node = parent

                else:

                    # Case: 5a
                    if node is parent.left and parent is gparent.left:
                        self.rotate_right(gparent)

                    # Case: 5b
                    elif node is parent.right and parent is gparent.right:
                        self.rotate_left(gparent)

                    parent.set_black()
                    gparent.set_red()

                    node = self.nil

    def remove(self, key):

        node = self.root

        while node is not self.nil and node.key != key:

            if key < node.key:
                node = node.left

            else: # key > node.key
                node = node.right

        if node is self.nil:
            return None

        else:

            parent = node.parent

            if node.left is self.nil: # takes care of the leaf case too
                self.transplant(node, node.right)

            elif node.right is self.nil:
                self.transplant(node, node.left)
                
            else:
                
                curr = node.right

                while curr.left is not self.nil:
                    
                    curr = curr.left

                successor = curr

                if successor.parent is node:
                    successor.right.parent = successor

                # TODO: finish implementing
                    
    def transplant(self, node, new_node):

        parent = node.parent

        if parent is self.nil:
            self.root = new_node

        elif parent.left is node:
            parent.left = new_node

        else: # parent.right is node
            parent.right = new_node

        new_node.parent = parent

    def print_structure(self):

        if self.root is self.nil:
            print("Tree is empty.")

        else:
            self._print_structure(self.root, "", True)

    def _print_structure(self, node, prefix, is_tail):

        if node is not self.nil:

            print(prefix + ("└──" if is_tail else "├── ") + str(node.key))

            prefix_add = "    " if is_tail else "│   "

            if node.left is not self.nil and node.right is not self.nil:
                self._print_structure(node.left, prefix + prefix_add, False)
                self._print_structure(node.right, prefix + prefix_add, True)
            else:
                self._print_structure(node.left, prefix + prefix_add, True)
                self._print_structure(node.right, prefix + prefix_add, True)


rbtree = RedBlackTree()
rbtree.add(10, 214)
rbtree.print_structure()
rbtree.add(14, 123)
rbtree.print_structure()
rbtree.add(235, 7)
rbtree.print_structure()
rbtree.add(9, "test")
rbtree.print_structure()
rbtree.add(98, "lol")
rbtree.print_structure()
rbtree.add(126)
rbtree.print_structure()
