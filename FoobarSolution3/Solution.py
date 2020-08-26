def to_decimal(n, b):
    sum = 0
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
        s = ""
        for c in sorted(n, reverse=True):
            s += c
        x = int(s)

        s = ""
        for c in sorted(n):
            s += c
        y = int(s)

        z = to_decimal(x, b) - to_decimal(y, b)
        z = to_base(z, b)
        n = str(z)

        while len(n) != length:
            n = "0" + n

        if n in lst:
            for value in cycle:
                if n == value:
                    return int(len(cycle))
            cycle.append(n)

        lst.append(n)
    # final!!
    return int(len(cycle))
