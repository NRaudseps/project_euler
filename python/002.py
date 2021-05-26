def fibonacci(n):
    sum = 0
    a, b = [1, 1]
    
    for i in range(n):
        if b < 4_000_000:
            a, b = b, a + b

            if a % 2 == 0:
                sum += a
                
    print(sum)

fibonacci(100)
