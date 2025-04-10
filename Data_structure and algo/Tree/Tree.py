class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self,child):
        self.children.append(child)
#traversel in tree
#pre order
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    for child in node.children:
        pre_order_traversal(child)
def depth_first_search(node,target):
    if node is None:
        return False
    if node.data == target:
        return True
    for child in node.children:
        if depth_first_search(child,target):
            return True
    return False
def insert_node(root,node):
    if root is None:
        root = node
    else:
        root.add_child(node)
def delete_node(root,target):
    if root is None:
        return None
    root.children = [child for child in root.children if root.children!=target]
    for child in root.children:
        delete_node(child,target)
def  tree_hight(node):
    if node is None:
        return 0
    if not node.children:
        return 1
    return 1+max(tree_hight(child) for child in node.children)




root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
print("Pre-order traversal:")
pre_order_traversal(root)



