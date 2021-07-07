import bin_tree_node


class BinTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value):

        if self.root is None:
            self.root = bin_tree_node.BinTreeNode(value)
            return self.root
        else:
            self.root.insert_node(value)

    def search(self, value):
        if self.root is not None:
            found = self.root.search_node(value)
            return found
        else:
            return None


tree = BinTree()
tree.insert(5)
tree.insert(6)
tree.insert(4)

print(tree.search(25))
