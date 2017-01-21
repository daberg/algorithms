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

        # Should check if node.right is not self.nil?

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

        # Should check if node.left is not self.nil?

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

            else:   # key > curr.key
                curr = curr.right

        if curr is self.nil:

            node = Node(key, data, True, self.nil, self.nil, self.nil)

            if parent is self.nil:
                self.root = node

            elif key < parent.key:
                parent.left = node
                node.parent = parent

            else:   # key > parent.key
                parent.right = node
                node.parent = parent

            self._fix_insert(node)

        else:   # curr.key == key

            curr.data = data

    def _fix_insert(self, node):

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

            else:   # key > node.key
                node = node.right

        if node is self.nil:
            return None

        else:

            # Like the _fix_remove function, this is directly took from the
            # CLRS book.

            y = node
            red = y.red

            if node.left is self.nil:
                x = node.right
                self.transplant(node, node.right)

            elif node.right is self.nil:
                x = node.left
                self.transplant(node, node.left)

            else:

                y = node.right

                while y.left is not self.nil:

                    y = y.left

                red = y.red
                x = y.right

                if y.parent is node:
                    x.parent = y

                else:

                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y

                self.transplant(node, y)

                y.left = node.left
                y.left.parent = y
                y.red = node.red

            if red is False:
                self._fix_remove(x)

    # This is basically just a Python implementation of the CLRS algorithm
    # to fix a RB tree deletion, almost no changes were made.
    def _fix_remove(self, node):

        while node is not self.root and node.is_black():

            if node is node.parent.left:

                sib = node.parent.right

                # Case 1
                if sib.is_red():

                    sib.set_black()
                    node.parent.set_red()
                    self.rotate_left(node.parent)
                    sib = node.parent.right

                # Case 2
                if sib.left.is_black() and sib.right.is_black():

                    sib.set_red()
                    node = node.parent

                # Case 3
                elif sib.right.is_black():

                    sib.left.set_black()
                    sib.set_red()
                    self.rotate_right(sib)
                    sib = node.parent.right

                # Case 4
                # It is mandatory to have another explicit "if" check here,
                # even if CLRS does not suggest it.
                elif sib.is_black() and sib.right.is_red():

                    sib.red = node.parent.red
                    node.parent.set_black()
                    sib.right.set_black()
                    self.rotate_left(node.parent)
                    node = self.root

            else:

                sib = node.parent.left

                # Case 5
                if sib.is_red():

                    sib.set_black()
                    node.parent.set_red()
                    self.rotate_right(node.parent)
                    sib = node.parent.left

                # Case 6
                if sib.right.is_black() and sib.left.is_black():

                    sib.set_red()
                    node = node.parent

                # Case 7
                elif sib.left.is_black():

                    sib.right.set_black()
                    sib.set_red()
                    self.rotate_left(sib)
                    sib = node.parent.left

                # Case 8
                # Here holds the same observation made for case 4.
                elif sib.is_black() and sib.left.is_red():

                    sib.red = node.parent.red
                    node.parent.set_black()
                    sib.left.set_black()
                    self.rotate_right(node.parent)
                    node = self.root

        node.set_black()

    # This function and the _old_fix_remove one do not work properly and are
    # there only to be possibly debugged for educational purposes.
    def _old_remove(self, key):

        node = self.root

        while node is not self.nil and node.key != key:

            if key < node.key:
                node = node.left

            else:   # key > node.key
                node = node.right

        if node is self.nil:
            return None

        else:

            # Case 1
            if node.left is not self.nil and node.right is not self.nil:

                curr = node.right

                while curr.left is not self.nil:

                    curr = curr.left

                successor = curr

                node.key = successor.key
                node.data = successor.data

                node = successor

            # Case 2
            if node.left is not self.nil and node.right is self.nil:
                child = node.left

            # Case 3 and end of case 1 and also case 0 (no children)
            else:   # node.left is self.nil or node.right is not self.nil
                child = node.right

            self.transplant(node, child)

            if node.is_black():
                self._old_fix_remove(child)

            # Probably useless
            # if node.parent is self.nil:
            #     self.root = child

    # This function and the _old_remove one do not work properly and are
    # there only to be possibly debugged for educational purposes.
    def _old_fix_remove(self, node):

        while node is not self.root and node.is_black():

            parent = node.parent

            # Cases: 1 - 2 - 3 - 4
            if node is parent.left:

                sib = parent.right
                slc = sib.left
                src = sib.right

                # Case 1
                if sib.is_red():
                    parent.set_red()
                    sib.set_black()
                    self.rotate_left(parent)

                else:

                    # Case 2
                    if slc.is_black() and src.is_black():
                        sib.set_red()
                        node = parent

                    # Case 3
                    elif slc.is_red() and src.is_black():
                        slc.set_black()
                        parent.set_red()
                        self.rotate_right(sib)

                    # Case 4
                    elif src.is_red():
                        sib.red = parent.red
                        parent.set_black()
                        src.set_black()
                        self.rotate_left(parent)
                        node = self.root

            # Cases: 5 - 6 - 7 - 8
            else:

                sib = parent.left
                slc = sib.left
                src = sib.right

                # Case 5
                if sib.is_red():
                    parent.set_red()
                    sib.set_black()
                    self.rotate_right(parent)

                else:

                    # Case 6
                    if slc.is_black() and src.is_black():
                        sib.set_red()
                        node = parent

                    # Case 7
                    elif slc.is_black() and src.is_red():
                        src.set_black()
                        parent.set_red()
                        self.rotate_left(node)

                    # Case 8
                    elif slc.is_red():
                        sib.red = parent.red
                        parent.set_black()
                        slc.set_black()
                        self.rotate_right(parent)
                        node = self.root

        if node is not self.nil:
            node.set_black()

    # TODO: make it throw exceptions
    def assert_validity(self):

        if self.nil.is_red():
            return False

        if self._assert_validity(self.root) is None:
            print("RB tree is not valid.")
            return False

        return True

    def _assert_validity(self, node):

        if node is self.nil:
            return 1

        if node.is_red() and (node.left.is_red() or node.right.is_red()):
            print(
                "Red node with key " +
                str(node.key) +
                " has at least one red children."
            )
            return None

        if ((node.left is not self.nil and node.key < node.left.key) or
                (node.right is not self.nil and node.key > node.right.key)):
            print("BST violation at node with key " + str(node.key) + ".")
            return None

        lbh = self._assert_validity(node.left)
        rbh = self._assert_validity(node.right)

        if lbh is not None and rbh is not None and lbh == rbh:

            if node.is_black():
                return lbh + 1

            else:
                return lbh

        else:
            return None

    def root_black_height(self):

        return self.black_height(self.root)

    def black_height(self, node):

        return self._black_height(node, True)

    def _black_height(self, node, is_first):

        if node is self.nil:

            if is_first:
                return 0

            else:
                return 1

        lbh = self._black_height(node.left, False)
        rbh = self._black_height(node.right, False)

        if lbh is not None and rbh is not None and lbh == rbh:

            if node.is_black() and not is_first:
                return lbh + 1

            else:
                return lbh

        else:
            return None

    def transplant(self, node, new_node):

        parent = node.parent

        if parent is self.nil:
            self.root = new_node

        elif node is parent.left:
            parent.left = new_node

        else:   # parent.right is node
            parent.right = new_node

        new_node.parent = parent

    def print_structure(self):

        if self.root is self.nil:
            print("Tree is empty.")

        else:
            self._print_structure(self.root, "", True)

    def _print_structure(self, node, prefix, is_tail):

        if node is not self.nil:

            node_type = "R" if node.is_red() else "B"

            print(prefix +
                  ("└──" if is_tail else "├── ") +
                  str(node.key) +
                  node_type)

            prefix_add = "    " if is_tail else "│   "

            if node.left is not self.nil and node.right is not self.nil:
                self._print_structure(node.left, prefix + prefix_add, False)
                self._print_structure(node.right, prefix + prefix_add, True)
            else:
                self._print_structure(node.left, prefix + prefix_add, True)
                self._print_structure(node.right, prefix + prefix_add, True)


if __name__ == "__main__":
    rbtree = RedBlackTree()
    rbtree.add(10, 214)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.add(14, 123)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.add(235, 7)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.add(9, "test")
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.add(98, "lol")
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.add(126)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    print("Start removing")
    rbtree.remove(10)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.remove(9)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.remove(126)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.remove(98)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.remove(235)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
    rbtree.remove(14)
    rbtree.print_structure()
    print(rbtree.assert_validity())
    print()
