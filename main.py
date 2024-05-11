class Tree:
    def __init__(self, key=None) -> None:
        self.key = key
        self.right = None
        self.left = None
    
    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        if key < self.key:
            if self.left is None:
                self.left = Tree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = Tree(key)
            else:
                self.right.insert(key)
    
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.key)
        if self.right is not None:
            self.right.print_tree()


tree = Tree()
tree.insert(1)
tree.insert(0)
tree.insert(11)
tree.print_tree()