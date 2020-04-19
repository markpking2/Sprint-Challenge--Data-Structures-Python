class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value:
            if target == self.value:
                return True
            elif target < self.value and self.left:
                return self.left.contains(target)
            elif target > self.value and self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        node = self
        while node.right:
            max = node.right.value
            node = node.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
