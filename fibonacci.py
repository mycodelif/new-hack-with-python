def fib(n):
    print(f'Calculate Fibonacci of {n}')
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
