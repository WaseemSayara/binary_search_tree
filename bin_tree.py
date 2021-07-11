import bin_tree_node


class BinTree:
    root = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        try:
            if self.root is None:
                self.root = bin_tree_node.BinTreeNode(int(float(value)))
                return True
            else:
                self.root.insert_node(int(float(value)))
                return True
        except ValueError:
            print("Wrong input entered ( " + str(value) + " ) Only numbers allowed.")
            return False

    def search(self, value):
        try:
            if self.root is not None:
                found = self.root.search_node(int(float(value)))
                return found
            else:
                return None
        except ValueError:
            print("Wrong input entered ( " + str(value) + " ) Only numbers allowed.")
            return False

    def print_tree_ascending(self):
        if self.root is None:
            print("the tree is empty")
            return None
        else:
            print("the tree values in ascending are: ")
            self.root.print_tree_node_ascending()
            return None

    def print_tree_descending(self):
        if self.root is None:
            print("the tree is empty")
            return None
        else:
            print("the tree values in descending are: ")
            self.root.print_tree_node_descending()
            return None

    def get_tree_ascending(self):
        if self.root is None:
            print("the tree is empty")
            return None
        else:
            arr = []
            return self.root.get_tree_node_ascending(arr)

    def get_tree_descending(self):
        if self.root is None:
            print("the tree is empty")
            return None
        else:
            arr = []
            return self.root.get_tree_node_descending(arr)


tree = BinTree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(2)
tree.insert(9)
tree.insert(3)
tree.insert("hg")
