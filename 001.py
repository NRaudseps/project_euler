def all_multiples(n):
    multiples = list()

    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return sum(multiples)


print(all_multiples(1000))
