from LinkedList import LinkedList
from Node import Node
class Queue:
    # constructs a new queue, which is bounded
    def __init__(self, max_size):
        self.lst = LinkedList()
        self.max_size = max_size
        self.current_size = 0

    # accessors
    def get_lst(self):
        return self.lst
    def get_max_size(self):
        return self.max_size
    def get_current_size(self):
        return self.current_size

    # adds a new Node object to the top of the stack
    def enqueue(self, node: Node):
        if self.get_current_size() > self.get_max_size():
            print("\n*** Queue Overflow ***")
            return

        self.lst.insert_node(self.get_current_size()+1, node)
        self.current_size += 1
        print("\nEnqueueing {}...\n{}".format(node, self.get_lst()))

    # removes the top node from the stack
    def dequeue(self):
        if self.get_current_size() == 0:
            print("\n*** Queue Underflow ***")
            return

        first = self.get_lst().get_head_node()
        self.lst.delete(0)
        print("\nDequeueing {}...\n{}".format(first, self.get_lst()))

        return first

    # returns and prints the top node of the stack without removing anything
    def peek(self):
        print("\nPeeping from stack...\n{}".format(self.get_lst().get_head_node()))
        return self.get_lst().get_head_node()

#tester
q = Queue(10)
q.dequeue()
print(q.lst)

for i in range(q.get_max_size()):
    q.enqueue(Node(i + 1, None))

q.peek()
q.dequeue()
q.enqueue(Node(11, None))
q.peek()