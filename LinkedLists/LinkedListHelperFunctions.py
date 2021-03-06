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
#############################################################
## count elements within a range

    def range(self, lo, hi):
        return self._range(lo, hi, self.head)

    def _range(self, lo, hi, pointer):
        if not pointer:
            return 0
        elif pointer.item <= hi and pointer.item >= lo:
            return 1 + self._range(lo, hi,pointer.next)
        return self._range(lo, hi, pointer.next)









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
## THIS CODE IS AN INTERNAL METHOD IE ACTS ON A LL, NOT PASSED A LL INSTANCE
    def even(self):
        return self.rcounteven(self.head, 0)


    def rcounteven(self, start_point, count = 0):
        if not start_point:
            return count
        elif not start_point.item % 2:
            return self.rcounteven(start_point.next, count + 1)
        return self.rcounteven(start_point.next, count)

#################################################################
## RECURSIVE MAX, BOTH OBFUSCATED AND NORMALLY ;)
    def rlargest(self):
        def _largest(node, current_max):
            if not node:
                return current_max
            if node.item > current_max:
                return _largest(node.next, node.item)
            return _largest(node.next, current_max)
        return _largest(self.head, self.head.item)

    def largest(self):
        return self._rlargest(self.head, self.head.item)

    def _rlargest(self, node, current_max):
        if not node:
            return current_max
        if node.item > current_max:
            return self._rlargest(node.next, node.item)
        return self._rlargest(node.next, current_max)


###############################################################
## CONSECUTIVE DUPLICATES -> TRUE ELSE FALSE
## USES A LAGGING TAIL RECURSIVE CONCEPT
    def consec(self):
        return self.rconsec(self.head, None)

    def rconsec(self, node, item):
        if not node:
            return False
        if node.item == item:
            return True
        return self.rconsec(node.next, node.item)


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
print(ll.range(0, 3))
