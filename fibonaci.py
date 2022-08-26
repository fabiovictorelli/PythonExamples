#! /usr/bin/python3.8
# My first Python
# Show Fibonacci Sequence
# fabiovictorelli@gmail.com
# Mon Aug 20 10:12:07 EDT 2022

def fib(n):
    print('fib  = ', end=' ')
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    print('fib2 = ', end=' ')
    a, b = 0, 1
    sum = a+b
    print(a, b, end=' ')
    while sum < n:
        print(sum, end=' ')
        a, b = b, sum
        sum = a+b
    print()


print("\nCalling 2 Functions Fibonacci:")
fib(1000)
fib2(1000)
