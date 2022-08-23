#! /usr/bin/python3.8
# My first Python


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
#        print ('a =' ,a, 'b =', b)
        a, b = b, a+b
    print()


# Chamando Fibonacci
print("\nChamando funcao Fibonacci:")
fib(1000)
