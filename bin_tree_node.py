class BinTreeNode:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def insert_node(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BinTreeNode(value)
            else:
                self.right.insert_node(value)

        elif value < self.value:
            if self.left is None:
                self.left = BinTreeNode(value)
            else:
                self.left.insert_node(value)
        else:
            return

    def search_node(self, value):
        if self is None:
            return None

        elif self.value == value:
            return self

        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.search_node(value)

        else:
            if self.right is None:
                return None
            else:
                return self.right.search_node(value)

    def print_tree_node_prefix(self):

        if self is None:
            return
        if self.left is not None:
            self.left.print_tree_node_prefix()
        print(self.value)
        if self.right is not None:
            self.right.print_tree_node_prefix()
        return

    def print_tree_node_postfix(self):

        if self is None:
            return
        if self.right is not None:
            self.right.print_tree_node_postfix()
        print(self.value)
        if self.left is not None:
            self.left.print_tree_node_postfix()
        return

    def get_tree_node_prefix(self, arr):

        if self is None:
            return
        if self.left is not None:
            self.left.get_tree_node_prefix(arr)
        arr.append(self.value)
        if self.right is not None:
            self.right.get_tree_node_prefix(arr)
        return arr

    def get_tree_node_postfix(self, arr):

        if self is None:
            return
        if self.right is not None:
            self.right.get_tree_node_postfix(arr)
        arr.append(self.value)
        if self.left is not None:
            self.left.get_tree_node_postfix(arr)
        return arr
