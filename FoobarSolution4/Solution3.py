from collections import deque
class Node:
    def __init__(self, lst, location : list, saldo): # a saldo is the number of walls that you can skip
        self.row = location[0]
        self.col = location[1]

        self.lst = lst
        self.saldo = saldo

    def get_pointers(self):
        pointers = []
        len_rows = len(self.lst)
        len_cols = len(self.lst[0])

        #left
        if self.col > 0:
            wall  = self.lst[self.row][self.col - 1] == 1 #checks to see if wall to left
            if wall:
                pointers.append(Node(self.lst, [self.row, self.col - 1], self.saldo - 1))
            else:
                pointers.append(Node(self.lst, [self.row, self.col - 1], self.saldo))

        #right
        if self.col < len_cols - 1:
            wall  = self.lst[self.row][self.col + 1] == 1 #checks to see if wall to right
            if wall:
                pointers.append(Node(self.lst, [self.row, self.col + 1], self.saldo - 1))
            else:
                pointers.append(Node(self.lst, [self.row, self.col + 1], self.saldo))

        # up
        if self.row > 0:
            wall = self.lst[self.row - 1][self.col] == 1  # checks to see if wall above
            if wall:
                pointers.append(Node(self.lst, [self.row - 1, self.col],
                                     self.saldo - 1))  # saldo is decreased by 1 because you have a wall that you can pass through
            else:
                pointers.append(Node(self.lst, [self.row - 1, self.col], self.saldo))

        # down
        if self.row < len_rows - 1:
            wall = self.lst[self.row + 1][self.col] == 1  # checks to see if there is a wall below
            if wall:
                pointers.append(Node(self.lst, [self.row + 1, self.col], self.saldo - 1))
            else:
                pointers.append(Node(self.lst, [self.row + 1, self.col], self.saldo))

        return pointers

class Graph:
    def __init__(self, lst, saldo):
        self.lst = lst
        self.len_rows = len(lst)
        self.len_cols = len(lst[0])
        self.saldo = saldo

    def get_path_cost(self):
        head_Node = Node(self.lst, [0,0], self.saldo)
        tail_Node = Node(self.lst, [self.len_rows - 1, self.len_cols-1], self.saldo)

        queue = deque([head_Node])
        cost_dict = {head_Node : 1}

        while queue:
            current_node = queue.popleft()
            if (current_node.row == tail_Node.row) and (current_node.col == tail_Node.col):
                return cost_dict[current_node]

            for pointer in current_node.get_pointers():
                if pointer not in cost_dict.keys():
                    cost_dict[pointer] = cost_dict[current_node] + 1
                    queue.append(pointer)

def solution(map):
    return Graph(map, 1).get_path_cost()

lst_1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
lst_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
#print(solution(lst_1))
#print(solution(lst_2))















