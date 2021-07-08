import bin_tree_node


class BinTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value):
        try:
            if self.root is None:
                self.root = bin_tree_node.BinTreeNode(int(value))
                return True
            else:
                self.root.insert_node(int(value))
        except ValueError:
            return False

    def search(self, value):
        if self.root is not None:
            found = self.root.search_node(value)
            return found
        else:
            return None

    def print_tree_prefix(self):
        if self.root is None:
            print("the tree is empty")
            return
        else:
            print("the tree values in prefix are: ")
            self.root.print_tree_node_prefix()
            return

    def print_tree_postfix(self):
        if self.root is None:
            print("the tree is empty")
            return
        else:
            print("the tree values in postfix are: ")
            self.root.print_tree_node_postfix()
            return

    def get_tree_prefix(self):
        if self.root is None:
            print("the tree is empty")
            return
        else:
            arr = []
            return self.root.get_tree_node_prefix(arr)

    def get_tree_postfix(self):
        if self.root is None:
            print("the tree is empty")
            return
        else:
            arr = []
            return self.root.get_tree_node_postfix(arr)


tree = BinTree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(2)
tree.insert(9)
tree.insert(3)
tree.insert("hg")
