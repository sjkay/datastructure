class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,tree,n):
        if self.root is None:
            self.root = n
        elif n.val < tree.val:
            if tree.left is None:
                tree.left = n
            else:
                self.insert(tree.left,n)
        else:
            if tree.right is None:
                tree.right = n
            else:
                self.insert(tree.right,n)
    def print(self,tree,level):
        if tree.right is not None:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val)
        if tree.left is not None:
            self.print(tree.left, level + 1)
    def inorder(self,tree):
        if tree is None:
            return
        else:
            self.inorder(tree.left)
            print(tree.val, end=' ')
            self.inorder(tree.right)
def main():
    bst = BST()
    bst.insert(bst.root, Node(8))
    bst.insert(bst.root, Node(6))
    bst.insert(bst.root, Node(3))
    bst.insert(bst.root, Node(14))
    bst.insert(bst.root, Node(12))
    bst.insert(bst.root, Node(6))
    bst.insert(bst.root, Node(10))
    bst.insert(bst.root, Node(14))
    bst.insert(bst.root, Node(12))
    bst.print(bst.root,0)
main()
