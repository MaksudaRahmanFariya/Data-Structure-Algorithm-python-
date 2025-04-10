import sys
class Node(object):
    def __init__(self, data):
        self.data = data                  # value store in this node
        self.left = None                  # pointer to the left child
        self.right = None                 # pointer to the right child
        self.height = 1                   # height of the node used for balancing
class AVL(object):
    def insert(self, root, key):
        if not root:
            return Node(key)                          # If the tree is empty, create a new node with the key
        if key < root.data:                           # recursively insert value if less than root
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)   # recursively insert value if greater than root
        # Update the height of the node after insertion
        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        balancefactor = self.getbalance(root)
        if balancefactor > 1:
            if key < root.left.key:
                return self.rightrotate(root)
            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)
        if balancefactor < -1:
            if key > root.right.key:
                return self.leftrotate(root)
            else:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)
        return root
    def leftrotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y
    def getheight(self, root):
        if not root:
            return 0
        return root.height
    def getbalance(self, root):
        if not root:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)
    def rightrotate(self, z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y
    def preorder(self, root):
        if not root:
            return 0
        print("{0} ".format(root.key), end="")
        self.preorder(root.left)
        self.preorder(root.right)

    def getminvalue(self, root):
        if root is None or root.left is None:
            return root
        return self.getminvalue(root.left)

    def delete_node(self, root, key):
        if not root:
            return 0
        elif key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getminvalue(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        if root is None:
            return root
        root.h = 1 + max(self.getheight(root.left), self.getheight(root.right))
        balancefactor = self.getbalance(root)
        if balancefactor > 1:
            if self.getbalance(root.left) >= 0:
                return self.rightrotate(root)
            else:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)
        if balancefactor < -1:
            if self.getbalance(root.right) <= 0:
                return self.leftrotate(root)
            else:
                root.right = self.rightrotate(root.left)
                return self.leftrotate(root)
        return root


        # Print the tree
    def printvalue(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.data)
            self.printvalue(currPtr.left, indent, False)
            self.printvalue(currPtr.right, indent, True)
myTree = AVL()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert(root, num)
myTree.printvalue(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printvalue(root, "", True)








