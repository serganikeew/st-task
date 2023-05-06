k = input()
x = k 

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact 

while factorial(x) != k:
    x = k - 1

print(factorial(x) == k)
