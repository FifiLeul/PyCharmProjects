from Node import Node
from LinkedList import LinkedList

class Stack:
    #constructs a new queue, which is bounded
    def __init__(self, max_size):
        self.lst = LinkedList()
        self.max_size = max_size
        self.current_size = 0

    #accessors
    def get_lst(self):
        return self.lst
    def get_max_size(self):
        return self.max_size
    def get_current_size(self):
        return self.current_size

    #adds a new Node object to the top of the stack
    def push(self, node: Node):
        if self.current_size != self.get_max_size():
            self.current_size += 1
            self.lst.insert_node(0, node)
            print("\nPushing {} to stack...\n{}".format(node, self.get_lst()))
            return

        print("\n*** Stack Overflow ***")

    #removes the top node from the stack
    def pop(self):
        old_head = self.get_lst().get_head_node()

        if self.get_current_size() == 0:
            print("\n*** Stack Underflow ***")
            return

        self.current_size += 1
        self.lst.delete(0)
        print("\nPopping {} from stack...\n{}".format(old_head, self.get_lst()))

        return old_head

    #returns and prints the top node of the stack without removing anything
    def peek(self):
        print("\nPeeping from stack...\n{}".format(self.get_lst().get_head_node()))
        return self.get_lst().get_head_node()


s= Stack(13);
s.pop();
print(s.lst);

for i in range(s.get_max_size() - 2):
    s.push(Node(i + 1, None))
s.pop();
s.push(Node(13, None))
s.peek();