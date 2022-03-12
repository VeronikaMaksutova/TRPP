import math as m

def main(x):
    q = 0
    for i in range(len(x)):
        j = int(i/3)
        q += m.pow(m.log10(7 * m.pow(x[j], 2) - m.pow(x[j], 3)), 5)

    return q * 79

print(main([-0.48, -0.67, 0.58, 0.85, 0.58]))
print(main([-0.27, -0.62, 0.27, 0.76, -0.54]))