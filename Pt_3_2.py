from functools import reduce

fib = lambda n, a=0, b=1: str(a) + " " + str(fib(n, b, a + b)) + " " if a <= n else ""
# fib = lambda n, a = 0, b = 1: [a] + fib(n, b, a+b) if a <= n else []

print(fib(int(input("Последовательность фибоначи до числа "))))
