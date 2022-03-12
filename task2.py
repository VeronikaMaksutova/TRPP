import math as s


def main(b, y, m, n):
    f = 0
    d = 0
    for i in range(b+1):
        if i == 0:
            continue
        f += ((s.pow((s.tan(1 - ((s.pow(y, 3))) / 72)), 5)) / 20.0) 
        f = f - s.pow(i, 2)
    for j in range(n+1):
        if j == 0:
            continue
        for k in range(m+1):
            if k == 0:
                continue
            d += (9 * s.pow(k, 3) + 29 * s.pow(j, 4) + s.pow(y, 2))
    return d + f
    


print(main(8, -0.01, 3, 7))