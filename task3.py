import math as m


def main(n):
    if n == 0:
        return -0.93
    else:
        return 12 * m.pow(m.sin(main(n-1)), 2) - main(n-1) - 94

print(main(4))
print(main(1))
