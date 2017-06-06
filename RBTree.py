class RBNode:
    def __init__(self, newval):
        self.val = newval
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None
    def search(self, k):
        x=self
        while x != None and k != x.val:
            if k < x.val:
                x = x.left
            else:
                x = x.right
        return x
    def minimum(self):
        x = self
        while x.left != None:
            x = x.left
        return x
    
class RBTree:
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
    def search(self, k):
        return self.root.search(k)
    def minimum(self):
        return self.root.minimum()
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
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
    bst = RBTree()
    bst.insert(bst.root, RBNode(5))
    bst.insert(bst.root, RBNode(2))
    bst.insert(bst.root, RBNode(-4))
    bst.insert(bst.root, RBNode(3))
    bst.insert(bst.root, RBNode(12))
    bst.insert(bst.root, RBNode(9))
    bst.insert(bst.root, RBNode(21))
    bst.insert(bst.root, RBNode(19))
    bst.insert(bst.root, RBNode(25))
    print('#####')
    bst.print(bst.root,0)
    print('#####')
    n = bst.search(12)
    bst.delete(n)
    bst.print(bst.root,0)
    print('#####')
    n = bst.search(5)
    bst.delete(n)
    bst.print(bst.root,0)
main()
