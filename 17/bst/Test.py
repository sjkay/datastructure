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
    def inorder_iter(self, tree):
        if tree is None:
            return
        stack = []
        current = tree
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if (len(stack)>0):
                    current = stack.pop()
                    print(current.val, end=' ')
                    current = current.right
                else:
                    break

def main():
    bst = BST()
    bst.insert(bst.root, Node(2))
    bst.insert(bst.root, Node(2))
    bst.insert(bst.root, Node(3))
    bst.insert(bst.root, Node(3))
    bst.insert(bst.root, Node(1))
    bst.insert(bst.root, Node(1))
    bst.print(bst.root,0)
    bst.inorder(bst.root)
    print()
    bst.inorder_iter(bst.root)
    print()
main()
