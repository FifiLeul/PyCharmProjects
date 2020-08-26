import math
from collections import deque


class MaxHeap:
    def __init__(self, root=None, max_size=10):
        self.root = root
        self.current_size = 0
        self.max_size = max_size

        if self.root == None:
            self.heap = []
        else:
            self.heap = [self.root]
            self.current_size = 1

    def push(self, child):
        if self.current_size < self.max_size:
            self.heap.append(child)
            self.current_size += 1
            # self.heapify_down()
            print("pushing {}...\n\theap: {}\n".format(child, self.heap))
            self.toStr()
        else:
            print("overflow")

    def pop(self):
        if self.current_size > 0:
            print("popping {}...\n\theap:\n".format(self.root))
            self.toStr()
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop(len(self.heap) - 1)
            self.current_size -= 1
            self.heapify_up(len(self.heap) - 1)
            print("popping {}...\n\theap: {}\n".format(self.root, self.heap))
            self.toStr()
        else:
            print("overflow")

    def peek(self):
        if self.current_size == 0:
            print("root: {}".format(self.root))
            return self.root
        else:
            print("overflow")

    def heapify_up(self, i):

        parent = math.floor(i / 2)
        smallest = i
        if parent >= 0 and self.heap[smallest] > self.heap[parent]:
            smallest = parent
        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.heapify_up(smallest)
        else:
            print("heapified....\n\theap:{}\n".format(self.heap))
            self.toStr()

    def heapify_down(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i

        if len(self.heap) < left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) < right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.heapify_down(largest)
        print("heapified....\n\theap:{}\n".format(self.heap))
        self.toStr()

    def toStr(self, i=0, level=0):
        num_levels = math.floor(int(self.current_size / 2))
        # print("levels: {}".format(num_levels))
        spaces_before = ""
        spaces_between = ""
        spaces_between_pairs= ""
        false_pair = True

        for j in range(int(self.spaces_bet(level))):
            spaces_between += " "
        for j in range(int(self.spaces_bet(level)) * 2 + 1):
                spaces_between_pairs += " "

        for j in range(int(self.spaces_before(level))):
            spaces_before += " "
        str_level = spaces_before

        if level == num_levels - 1:
            for j in self.heap[i:]:
                str_level += str(j) + spaces_between
            print(str_level)
            return

        len_level = int(math.pow(2, level))
        for j in range(len_level):
            if i + j > self.current_size - 1:
                self.toStr(i, level + 1)
                return
            if len_level / 2 == 1:
                str_level += str(self.heap[i + j]) + spaces_between_pairs
            elif j % 2 == 0 and false_pair == False:
                str_level += str(self.heap[i + j]) + spaces_between_pairs
                false_pair = not false_pair
            else:
                str_level += str(self.heap[i + j]) + spaces_between
        i += int(math.pow(2, level))
        print(str_level)
        self.toStr(i, level + 1)

    def spaces_bet(self, level):
        num_levels = math.floor(int(self.current_size / 2))
        return (num_levels - level) * 2 + 1
    def spaces_before(self,level):
        num_levels = self.get_levels()
        if num_levels <= level:
            return 0
        else:
            return self.spaces_before(level + 1) * 2 + 1

    def get_levels(self, levels=0, power=0):
        if power >= self.current_size:
            return levels
        return self.get_levels(levels + 1, math.pow(2, levels + 1) - 1)


heap = MaxHeap(40, 20)
heap.push(20)
heap.push(35)
heap.push(16)
heap.push(19)
heap.push(13)
heap.push(15)
heap.push(17)
heap.push(18)
heap.push(12)
heap.push(4)
heap.push(8)
heap.push(6)

