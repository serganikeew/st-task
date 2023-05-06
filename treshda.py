k = input()
n = 0

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact 

while factorial(n) != k:
    n = n + 1 
