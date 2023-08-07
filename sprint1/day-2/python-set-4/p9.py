# Invert the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

def printTree(root):
    if root is not None:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


inverted_root = invertTree(root)
printTree(inverted_root)
