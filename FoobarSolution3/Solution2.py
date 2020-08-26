def to_decimal(n, b):
    sum = 0
    n = int(n)
    k = len(str(n))
    if b == 10:
        return n
    for digit in str(n):
        k -= 1
        sum += int(digit) * (b ** k)
    return sum

def to_base(n, b):
    m = ""
    n = int(n)
    while n != 0:
        d = int(n / b)
        r = n % b
        m = str(r) + m

        n = d
    return m

def solution(n, b):
    no_repeats = True
    lst = [n]
    length = len(n)
    cycle = []

    while no_repeats:
        x = "".join(sorted(n, reverse = True))
        y = "".join(sorted(n, reverse = False))
        #print("x: {}, y: {}".format(x, y))
        z = to_decimal(x, b) - to_decimal(y, b)
        z = to_base(z, b)

        n = str(z)
        while len(n) != length:
            n = "0" + n

        if n in lst:
            if n in cycle:
                return int(len(cycle))
            cycle.append(n)

        lst.append(n)
    # final!!
    return int(len(cycle))
    #return int(len(cycle))
#much cleaner!!

print(solution('210022', 3))
print(solution('1211', 10))
