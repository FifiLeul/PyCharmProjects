'''

import Solution3

print(Solution3.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(Solution3.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
'''

from collections import deque
import time
class Node:
    def __init__(self, lst, location, saldo): # a saldo is the number of walls that you can skip
        self.row = location[0]
        self.col = location[1]

        self.lst = lst
        self.saldo = saldo
    def equals(self, other_node):
        return (self.row == other_node.row) and (self.col == other_node.col)
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
                pointers.append(Node(self.lst, [self.row - 1, self.col], self.saldo - 1))  # saldo is decreased by 1 because you have a wall that you can pass through
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
        head_node = Node(self.lst, [0,0], self.saldo)
        tail_node = Node(self.lst, [self.len_rows - 1, self.len_cols-1], self.saldo)

        queue = deque([head_node])
        cost_dict = {head_node : 1}

        while queue:
            current_node = queue.popleft()

            if current_node.equals(tail_node):
                return cost_dict[current_node]

            for pointer in current_node.get_pointers():
                if pointer not in cost_dict.keys():
                    cost_dict[pointer] = cost_dict[current_node] + 1
                    queue.append(pointer)
        return "infinite"

def solution(map):
    return Graph(map, 1).get_path_cost()


lst_1 = [[0, 1, 1, 0],
         [0, 0, 0, 1],
         [1, 1, 0, 0],
         [1, 1, 1, 0]]
lst_2 = [[0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0]]
lst_3 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(lst_1))
print(solution(lst_2))
print(solution(lst_3))
'''

import time
from collections import deque


class Node:

    def __init__(self, x, y, saldo, grid):
        self.x = x
        self.y = y;
        self.saldo = saldo
        self.grid = grid

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        saldo = self.saldo
        grid = self.grid
        rows = len(grid)
        columns = len(grid[0])

        if x > 0:
            wall = grid[y][x - 1] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x - 1, y, saldo - 1, grid))
            else:
                neighbors.append(Node(x - 1, y, saldo, grid))

        if x < columns - 1:
            wall = grid[y][x + 1] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x + 1, y, saldo - 1, grid))
            else:
                neighbors.append(Node(x + 1, y, saldo, grid))

        if y > 0:
            wall = grid[y - 1][x] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x, y - 1, saldo - 1, grid))
            else:
                neighbors.append(Node(x, y - 1, saldo, grid))

        if y < rows - 1:
            wall = grid[y + 1][x]
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x, y + 1, saldo - 1, grid))
            else:
                neighbors.append(Node(x, y + 1, saldo, grid))

        return neighbors


class GridEscapeRouter:

    def __init__(self, grid, saldo):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.saldo = saldo

    def get_escape_route_length(self):
        source = Node(0, 0, self.saldo, self.grid)
        queue = deque([source])
        distance_map = {source: 1}

        while queue:
            current_node = queue.popleft()

            if current_node.x == self.columns - 1 and\
                current_node.y == self.rows - 1:
                return distance_map[current_node]

            for child_node in current_node.get_neighbors():
                if child_node not in distance_map.keys():
                    distance_map[child_node] = distance_map[current_node] + 1
                    queue.append(child_node)

        #return 1000 * 1000 * 1000 # Cannot escape

def milliseconds():
    return int(round(time.time() * 1000))


start_time = milliseconds()
router = GridEscapeRouter(
    [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    1)

route_length = router.get_escape_route_length();
end_time = milliseconds()

print("Route length", route_length, "in", end_time - start_time, "milliseconds.")

router = GridEscapeRouter([[0, 1, 1, 0],
                           [0, 0, 0, 1],
                           [1, 1, 0, 0],
                           [1, 1, 1, 0]],
                          1)
print(router.get_escape_route_length())

router = GridEscapeRouter([[0, 0, 0, 0, 0, 0],
                           [1, 1, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 1, 1],
                           [0, 1, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0]],
                          1)

print(router.get_escape_route_length())
'''

