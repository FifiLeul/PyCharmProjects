def lst_diffs(lst):
    diffs = []
    for i in range(len(lst) - 1):
        diffs.append(lst[i + 1] - lst[i])
    return diffs


def lst_multiples(lst):
    diffs = []
    for i in range(len(lst) - 1):
        diffs.append(lst[i + 1] / lst[i])
    return diffs


def sigma(start, end):
    sum = 0
    for n in range(start, end + 1):
        sum += -4 * ((-5) ** (n - 1))
    return sum


def as_comm_diff(a_one, n, d):
    return (n / 2) * ((2 * a_one) + (n - 1) * (d))


def as_index(a_one, n, index):
    return (n / 2)(a_one + index)


def gs(a_one, n, r):
    return (a_one * (1 - (r ** n))) / (1 - r)


def gs_infinite_eval(gs):
    r = lst_multiples(gs)[0]
    print(r)
    if abs(r) < 1:
        return "Converges: " + str(gs[0] / (1 - r))
    else:
        return "Diverges: " + str(gs[0] / (1 - .5))


lst = [6, -3 / 2, 3 / 8, -3 / 32]
print("List Differences: " + str(lst_diffs(lst)))
print("List Multiples: " + str(lst_multiples(lst)))

print("Sigma: " + str(sigma(1, 7)))
print("Arithmetic Sequence with D: " + str(as_comm_diff(-1, 14, 9)))
# print(as_index())
print("Geometric Sequences: " + str(gs(-2, 9, lst_multiples([-2, - 8, - 32, - 128])[0])))
print("Geometric Infinite Evaluations: " + gs_infinite_eval([729, 729/3]))