class Node:
    '''
    * value
    * point to something else, can do a list of references
    * name
    '''
    def __init__(self, location, value, pointers = []):
        self.location = location
        if value == 1:
            self.pointers = None
        else:
            self.pointers = pointers
    def get_pointers(self):
        return [pointer.location for pointer in self.pointers]
    def add_pointer(self, pointer):
        self.pointers.append(pointer)
    #def __repr__(self):
        #return self.location

class Graph:
    def __init__(self):
        self.vertices = []
    '''
    * directed or not directed
    * list of nodes, which = vertices
    * pointers = edges
    * cost always == 1   
    * can add vertex, add edges (directional/non-directional) 
    '''
def create_lst(lst):
    nulls_and_valids = [] # one list; index 1 is the 1s, index 0 is the 0s with pointers
    for rows in range(len(lst)):
        r = []

        for cols in range (len(lst[rows])):
            if lst[rows][cols] == 1:
                r.append(Node("{},{}".format(rows,cols),1))
                continue

            index = lst[rows][cols]
            r.append(Node("{},{}".format(rows,cols), index, create_pointers(lst, rows, cols)))

        nulls_and_valids.append(r)

    return nulls_and_valids
def create_pointers(lst, rows, cols):
    pointers = []

    try:
        index = lst[rows+1][cols] #down
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    try:
        index = lst[rows-1][cols] #up
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    try:
        index = lst[rows][cols-1] #left
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    try:
        index = lst[rows][cols+1] #right
        print(index)
        if index != 1:
            pointers.append(index)
    except:
        pass

    #print(pointers)
    return pointers

lst_1 = create_lst([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
lst_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

lst_2 = create_lst(lst_2)
for row in lst_2:
    print(row)

def path(lst):
    curr = lst[0][0]
    count = 0
    while True:
        if curr.pointers != None and curr.pointers != []:
            print("Moving from ({}) to ({})".format(curr, curr.pointers[0]))
            curr = curr.pointers[0]
            count += 1
        if curr == lst[len(lst)-1][len(lst[0])-1]:
            print("we have finally arrived at the end: {}".format(curr))
            return count
        else:
            print("the path has ended at {}".format(curr))
            return count

print(path(lst_2))
print(lst_2[0][0].pointers)
'''def show_target( lst, row, col):
    r = lst[row]
    r[col] = " * "lst
    for level in range(len(lst)):
        for column in range(len(lst[level])):
            lst[level][column] = str(lst[level][column])
        print(lst[level])
'''
#show_target(create_lst(lst_2), 2,2)
#print("\n{}".format(create_lst(lst_2)[2][2].pointers))