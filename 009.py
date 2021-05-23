import math

#print(math.isqrt(4) ** 2 == 4)

def check_perfect_square(n):
    return n == math.isqrt(n) ** 2

triplets = list()
max_num = 1000
for a in range(1, max_num):
    for b in range(1, max_num):
        c = a**2 + b**2
        if check_perfect_square(c):
            triplets.append([a, b, int(math.sqrt(c))])

            if sum(triplets[-1]) == 1000:
                print(triplets[-1][0] * triplets[-1][1] * triplets[-1][2])
                print(triplets[-1])

