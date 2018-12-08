#NOT THE BEST IMPLEMENTATION OF A LINKEDLIST
#OBFUSCATED SHIT ADDS EVERYTHING TO THE FRONT 
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next 
            return item

    def is_empty(self):
        return self.head == None

#class LinkedStack:
 #   def __init__(self):
  #      self.stack = LinkedList()

   # def push(self, item):
    #    self.stack.add(item)

    #def pop(self):
     #   return self.stack.remove()

    #def isempty(self):
     #   return self.stack.is_empty()



##### New Functions Below, some are useful, others not #####
## LENGTH FUNCTIONS
## SAME AS COUNT ELEMS
    def rlength(self):
        def _rlength(node):
            return 0 if not node else 1 + _rlength(node.next)
        return _rlength(self.head)

    def count(self):
        return self._count(self.head)
    def _count(self, node):
        return 0 if not node else 1 + self._count(node.next)
############################################################
## CONTAINS FUNCTIONS
    def contains(self, item):
        pointer = self.head
        while pointer.next is not None:
            if pointer.item == item:
                return True
            pointer = pointer.next
        return False
    def rcontains(self, item):
        def _rcontains(node):
            if not node:
                return False
            return True if node.item == item else rcontains(node.next)
        return rcontains(self.head)

    def isthere(self,node, item):
        if not node:
            return False
        return True if node.item == item else self.isthere(node.next, item)

    def risthere(self, item):
        return self.isthere(self.head, item)

################################################################
## RETURN NEXT ITEM OF A NODE GIVEN NODE VALUE
    def after(self, item):
        current = self.head
        while current and current.item != item:
            current = current.next
        return current.next.item if current else None

##############################
## RETURN PREVIOUS ITEM OF NODE GIVEN NODE VALUE
    def before(self, item):
        previous = None
        current = self.head
        while current and current.item != item:
            previous = current
            current = current.next
        return previous.item if current else None




    def _before(self, item):
        return self.rbefore(self.head, item)


    def rbefore(self, node, item, previous = None):
        if not Node:
            return None
        if node.item == item:
            return previous
        return self.rbefore(node.next, item, node.item)

    def before(self, n):
        def _before(node, previous=None):
            if node is None:
                return None
            if node.item == n:
                return previous
            return _before(node.next, node.item)
        return _before(self.head)
#################################################
## RECURSIVELY PRINT A LINKEDLIST


    def print_list(self):
        def rprint(node):
            if not node:
                return
            else:
                print(node.item)
                rprint(node.next)
        return rprint(self.head)

##################################################################
## ADD ITEM TO THE END

    def endadd(self, item):
        pointer = self.head
        if pointer:
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(item, None)
        else:
            self.head = Node(item, None)


################################################################
## rotate a linked list


    def rotate(self):
        new_end = self.remove()
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = Node(new_end, None)

    ## optimised code below if we have a written endadd function

    def rrotate(self):
        new_end = self.remove()
        self.endadd(new_end)





#################################################################
## reverse a linked list



    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


################################################################
## sort a linkedlist

    def _sort(self):
        if self.count() > 1:
            intermediate = []
            current_node = self.head
            intermediate.append(current_node.item)
            while current_node.next:
                current_node = current_node.next
                intermediate.append(current_node.item)
            intermediate = sorted(intermediate, reverse = True)
            sorted_ll = LinkedList()
            for i in range(len(intermediate)):
                sorted_ll.add(intermediate[i])
            return sorted_ll
        else:
            return []


###############################################################
## DETECT A LIST WITH DUPLICATE POINTERS TO HEAD

    def loopy(llinstace):
        root = llinstace.head
        pointer = llinstace.head
        while pointer:
            if pointer.next and pointer.next == root:
                return True
            pointer = pointer.next
        return False




######################################
## COUNT EVEN ELEMENTS OF A LINKED LIST
def even_count(llinstace, count):
    return reven(llinstace.head, 0)

def reven(node, count):
    if not node:
        return count
    if not node.item % 2:
        return reven(node.next, count + 1)
    return reven(node.next, count)


def reven_count(lst):
    def _even_count(node, count):
        if not node:
            return count
        elif node.item % 2 == 0:
            return _even_count(node.next, count +1)
        else:
            return _even_count(node.next, count)
    return _even_count(lst.head, 0)

















ll = LinkedList()
ll.add(2)
ll.add(3)
ll.add(4)
ll.print_list()
print("reversing now")
ll = ll._sort()
ll.print_list()
#print(reven_count(ll))
