def is_palindrome(n):
    return True if str(n) == str(n)[::-1] else False

largest_number = list() 
for i in range(100, 999):
    for j in range(100, 999):
        if is_palindrome(i * j):
            print(i,  j)
            largest_number.append(i * j)

print(max(largest_number))
