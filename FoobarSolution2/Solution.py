def get_end_num_x(x):
    lst = [1]
    i = 1
    incrementation = 1
    for l in range(x):
        lst.append(lst[i - 1] + incrementation + 1)
        i += 1
        incrementation += 1
    return lst[-1]
def get_end_num_y(y):
    lst = [1]
    i = 1
    incrementation = 1
    for l in range(y-1):
        lst.append(lst[i - 1] + incrementation)
        i += 1
        incrementation += 1
    return lst
get_end_num_y(4)
def make_level(start_num, end_num, level_num):
    lst = [start_num]
    i = 1
    incrementation = level_num
    while end_num not in lst:
        lst.append(lst[i-1] + incrementation+1)
        i += 1
        incrementation += 1
    return lst

def get_rows(e):
    level = 1
    starting_num = 1
    ending_num = e
    levels = []
    current_level = make_level(starting_num, ending_num, level)
    height = len(current_level)
    levels_made = 0
    while levels_made < height:
        levels.append(current_level)
        levels_made += 1
        try:
            starting_num = current_level[1] - 1
        except:
            break
        ending_num -=1
        level += 1
        current_level = make_level(starting_num, ending_num, level)
    return levels

def get_cols(e):
    levels = get_rows(e)
    columns = []
    ending_num = e
    current_level = make_level(1, ending_num, 1)
    height = len(current_level)

    for j in range(height):
        col = []
        for i in range(len(levels)):
             if len(levels[i]) >= j+1:
                col.append(levels[i][j])
        columns.append(col)
    return columns

def solution(x,y):
    if x > y:
        end = get_end_num_x(x+y)
    else:
        top_of_pyramid = get_end_num_y(x-1 + y)
        end = top_of_pyramid[-1] + len(top_of_pyramid) -1

    rows = get_rows(end)
    cols = get_cols(end)

    for i in reversed(range(len(rows))):
        print("{}: {}".format(i+1, rows[i]))
    print(cols[x-1])

    return cols[x-1][y-1]


#print(solution(500,5))
#print(solution(3,2))
#(solution(5,10))
print(solution(50, 5))
#lst = get_end_num_y((2-1)+3)
#print(lst[-1]+ len(lst)-1)