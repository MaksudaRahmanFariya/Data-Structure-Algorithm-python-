class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        # If data == self.data, we do nothing (no duplicates)

    def printree(self):
        if self.left:
            self.left.printree()
        print(self.data)
        if self.right:
            self.right.printree()
    def inorderTraversal(self,root):

        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        #print(res)
        return res
    def preorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res
        #print(res)
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)
        return res
    def findvalue(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " is not found"
            return self.left.findvalue(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + "is not found"
            return self.right.findvalue(value)
        else:
            print(str(self.data) + ' is found')


# left->root->right
# root->left->right


root = Node(12)
root.insert(14)
root.insert(11)
root.insert(10)
root.insert(9)
root.insert(31)
root.insert(42)

print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
ele = 17
print("\nElement to be searched: ", ele)
print(root.findvalue(ele))
#root.printree()
