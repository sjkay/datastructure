BLACK = 0
RED = 1

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
        self.sentinel = RBNode()
        self.sentinel.left = self.sentinel.right = self.sentinel
        self.sentinel.color = BLACK
        self.sentinel.nonzero = 0
        self.root = self.sentinel
        self.count = 0
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
    def insertNode(self, key, value):
        current = self.root
        parent = None
        while current != self.sentinel:
            rc = self.__cmp(key, current.key)
            if rc == 0:
                return current
            parent = current
            if rc < 0:
                current = current.left
            else:
                current = current.right
        x = RBNode(key, value)
        x.left = x.right = self.sentinel
        x.parent = parent
        self.count = self.count + 1
        if parent:
            if self.__cmp(key, parent.key) < 0:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x
        self.insertFixup(x)
        return x
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
    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y
        y.left = x
        if x != self.sentinel:
            x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.sentinel:
            y.right.parent = x
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        else:
            self.root = y
        y.right = x
        if x != self.sentinel:
            x.parent = y


class RBTreeIter(object):

    def __init__ (self, tree):
        self.tree = tree
        self.index = -1  # ready to iterate on the next() call
        self.node = None
        self.stopped = False

    def __iter__ (self):
        """ Return the current item in the container
        """
        return self.node.value

    def next (self):
        """ Return the next item in the container
            Once we go off the list we stay off even if the list changes
        """
        if self.stopped or (self.index + 1 >= self.tree.__len__()):
            self.stopped = True
            raise StopIteration
        #
        self.index += 1
        if self.index == 0:
            self.node = self.tree.firstNode()
        else:
            self.node = self.tree.nextNode (self.node)
        return self.node.value

    def insertFixup(self, x):
        while x != self.root and x.parent.color == RED:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.color == RED:
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.rotateLeft(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateRight(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color == RED:
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.rotateRight(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateLeft(x.parent.parent)

        self.root.color = BLACK


def main():
    bst = RBTree()
    bst.insert(bst.root, RBNode(5))
    bst.insert(bst.root, RBNode(2))
    bst.insert(bst.root, RBNode(-4))
    bst.insert(bst.root, RBNode(3))
    bst.insert(bst.root, RBNode(12))
    bst.insert(bst.root, RBNode(9)
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
