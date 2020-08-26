import Node

# TODO: priority queue with the most pressing being the root of the tree
''' 
    * can use a list or a linked list, any sequential data structure

    * formulas for indexes
        * left child: (index * 2) + 1
        * right child: (index * 2) + 2
        * parent: (index - 1) / 2 

    * properties:
        * specify length
        * get index of new node
        * add element
            * involves heapifying up 
        * remove element
            * involves heapifying down 
        * heapify up
        * heapify down


'''

class Heap:
    def __init__(self, max_size = 10, root = None):
        self.root = root
        if self.root is None:
            self.heap = LinkedList()
            self.index = -1
        else:
            self.current_size = 0
            self.heap = [root]
            self.index = 0
        self.max_size = max_size

    def get_root(self):
        return self.root
    def last_parent(self):
        self.index = int((self.index - 1) / 2)
        return self.heap[self.index]
    def get_left_child(self):
        if int((self.index * 2) + 1) <= self.max_size:
            self.index = int((self.index * 2) + 1)
            try:
                return self.heap[self.index]
            except IndexError:
                return "child does not exist"
        return IndexError("no more space left")
    def get_right_child(self):
        if int((self.index * 2) + 2) + 1 <= self.max_size:
            self.index = int((self.index * 2) + 2)
            try:
                return self.heap[self.index]
            except IndexError:
                return "child does not exist"
        return IndexError("no more space left")
    def add_parent(self):
        if int((self.current_size - 1) /2) < max.size:
            self.index = int((self.current_size - 1) /2)
            return self.heap[self.index]
        return IndexError("overflow: no space for new parent")

    def add_left_child(self, child):
        if int((self.index * 2) + 2) + 1 <= self.max_size:
            self.index = int((self.index * 2) + 2)
            self.heap[self.index] =  child
            self.heapify()
            return "inserting {}".format(child)
        return IndexError("overflow: no space for new child")
    def add_right_child(self, child):
        if int((self.current_size - 1) / 2) < max.size:
            self.index = int((self.current_size - 1) / 2)
            self.heapify()
            return "inserting {}".format(child)
        return IndexError("overflow: no space for new child")
    def has_child(self):
        if self.get_left_child() != "child does not exist" and self.get_right_child() != "child does not exist":
            return 1, True
        if self.get_left_child() != "child does not exist":
            return 2, True
        if self.get_right_child() != "child does not exist":
            return 3, True
        return -1, False
    def heapify(self):
        current_node = self.get_root()
        while self.has_child():
            next = self.get_right_child()
            if next.get_data() > current_node.get_data():
                switcher = next
                next = current_node
                current_node = next
            if self.has_child() == 1 or self.has_child() == 2:
                next = self.get_left_child()
                if next.get_data() > current_node.get_data():
                    switcher = next
                    next = current_node
                    current_node = next
            else:
                current_node = curren

















