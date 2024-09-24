"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
"""
fib = [0,1,0]

print(fib)
n = 6
i = 2
while i <= n:
    fib[i] = fib[i-1] + fib[i-2]
    fib.append(fib[i])
    i+=1

print(fib[4])