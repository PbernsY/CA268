class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)



##########################################################################
    def size_of_tree(self):
        return self.count(self.root)

    def count(self, pointer):
        if not pointer:
            return 0
        else:
            return 1 + self.count(pointer.left) + self.count(pointer.right)
    def rcount(self):
        def _rcount(node):
            return 0 if not node else 1 + _rcount(node.left) + _rcount(node.right)
        return _rcount(self.root)

############################################################################
## Height of a binary tree

    def height(self):
        return self.rheight(self.root)

    def rheight(self, pointer):
        if not pointer:
            return 0
        else:
            return 1 + max(self.rheight(pointer.left), self.rheight(pointer.right))
    def _height(self):
        def _(node):
            return 0 if not node else 1 + max(_(node.left), _(node.right))
        return _(self.root)
###############################################################################
## count range of elements

    def range(self, lo , hi):
        return self._range(lo, hi, self.root)

    def _range(self,lo, hi, node):
        if not node:
            return 0
        if node.item <= hi and node.item >= lo:
            return 1 + self._range(lo, hi, node.left) + self._range(lo, hi, node.right)
        elif node.item < lo:
            return self._range(lo, hi, node.right)
        else:
            return self._range(lo, hi, node.left)




#################################################################################
## christmas tree presents


    def present(self, item):
        return self.rpresent(self.root, item)

    def rpresent(self, node, item):
        if not node:
            return False
        if node.item == item:
            return True
        elif node.item < item:
            return self.rpresent(node.right, item)
        else:
            return self.rpresent(node.left, item)

##################################################################################
## sum elements of a tree


    def tsum(self):
        return self._tsum(self.root)

    def _tsum(self, pointer):
        if not pointer:
            return 0
        else:
            return pointer.item + self._tsum(pointer.left) + self._tsum(pointer.right)
#################################################################################
## COUNT NUMBER OF LEAVES


    def leafc(self):
        return self.rleafc(self.root)

    def rleafc(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.rleafc(node.left) + self.rleafc(node.right)


    def recursive_leaf(self, ptr):
        if ptr == None:  # Base Case
            return 0
        if ptr.left == None and ptr.right == None:
            return 1 + self.recursive_leaf(ptr.left) + self.recursive_leaf(ptr.right)
        else:
            return self.recursive_leaf(ptr.left) + self.recursive_leaf(ptr.right)

    def count_leaves(self):
        return self.recursive_leaf(self.root)
        
##############################################################################
## make a balanced tree from a list 
    def make_list(lst):
        if len(lst) <= 2:
            return lst
        lst = sorted(lst)
        mid = len(lst) // 2
        return [lst[mid]] + make_list(lst[:mid]) + make_list(lst[mid + 1:])

##############################################################################
## test for a maximal tree

    def is_maximal(self):
        return ((2 ** int(bst.height) - 1) == int(bst.count()))

###############################################################################
## IN ORDER TRAVERSAL
    def inorder(self):
        return self.in_order(self.root)

    def in_order(self, start):
        if not start:
            return 
        self.in_order(start.left)
        print(str(start.item))
        self.in_order(start.right)
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, start):
        if start:
            print(start.item)
            self._preorder(start.left)
            self._preorder(start.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, start):
        if start:
            self._postorder(start.left)
            self._postorder(start.right)
            print(start.item)

    def balanced(self):
        if not self.root:
            return
        return True if abs(self.rheight(self.root.left) - self.rheight(self.root.right)) <= 1 else False

tree = BST()

tree.add(2)
tree.add(1)
tree.add(3)
tree.add(4)
tree.add(7)
print(tree.balanced())