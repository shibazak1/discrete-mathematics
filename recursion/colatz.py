def collatz(n):
    assert n >= 1
    if n == 1:
        return 0
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)
