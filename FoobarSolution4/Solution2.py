class Node(object):
    def __init__(self, location, value, pointers = [] ):
        self.location = location
        self.row = location[0]
        self.col = location[1]

        self.value = value
        if value == 1:
            self.pointers = None
        else:
            self.pointers = pointers

    def get_row(self):
        return self.row
    def get_col(self):
        return self.col

    def set_pointers(self, new_pointers: list):
        if self.value == 1:
            self.pointers = None
        self.pointers = new_pointers
    def remove_pointer(self, pointer):
        if pointer in self.pointers:
            self.pointers.remove(pointer)

def create_pointers(lst, rows, cols):
    pointers = []

    try:
        index = Node(rows, cols, lst[rows+1][cols]) #down
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass
    try:
        index = lst[rows][cols + 1]  # right
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    try:
        index = Node(rows, cols, lst[rows][cols-1]) #left
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    try:
        index = Node(rows, cols, lst[rows-1][cols]) #up
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass
    return pointers
def answer(lst):
    path_len = 0
    i = Node([0, 0], lst[0][0])
    #print(i)
    #r = i.get_row()
    #c = i.get_col()
    while i.location[0] < len(lst) and i.col < len(lst[0]):
        i.set_pointers(create_pointers(lst, i.row, i.col))
        if len(i.pointers) > 0:
            i = i.pointers[0]
        path_len += 1
    return path_len

lst_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(answer(lst_2))


def sorted(lst):
    sorted_rows = []
    current_row = lst[0].row
    row_elements = []

    for i in range(len(lst)):
        while lst[i].row == current_row:
            row_elements.append(lst[i])
            i += 1
        sorted_rows.append(mergeSort(row_elements))
    return sorted_rows

def mergeSort(lst):
   if len(lst) > 1:
    middle = int(len(lst)/2)
    left = lst[:middle]
    right = lst[middle:]

    mergeSort(left)
    mergeSort(right)

    lst_index = r = l = 0

    while r < len(right) and l < len(left):
        if left[l] < right[r]:
            lst[lst_index] = left[l]
            l += 1
        else:
            lst[lst_index] = right[r]
            r += 1
        lst_index += 1
    while l < len(left):
        lst[lst_index] = left[l]
        l += 1
        lst_index += 1

    while r < len(right):
        lst[lst_index] = right[r]
        r += 1
        lst_index += 1
    return lst
print(mergeSort([32,5,432,5,2,1,4,4,751,454,2134548,11,2]))