class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else: self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def show_tree(self):
        if self.left:
            self.left.show_tree()
        print(self.data)

        if self.right:
            self.right.show_tree()
    
    def search(self, value):
        if value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(value)

        elif value > self.data:
            if self.right is None:
                return False
            else:
                return self.right.search(value)

        else:
            return True
        


def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


Tree = Node(10)
Tree.insert(11)
Tree.insert(9)

Tree.insert(2)
Tree.insert(5)
Tree.insert(7)
Tree.insert(24)
Tree.insert(19)
Tree.insert(3)
Tree.insert(2)
Tree.insert(23)
print(Tree.data)
Tree.show_tree()
print(Tree.search(24))
print(Tree.search(1))
