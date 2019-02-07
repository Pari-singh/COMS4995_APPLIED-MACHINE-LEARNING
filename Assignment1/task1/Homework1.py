def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = 1
        last = 0
        for i in range(2,n+1):
            num = last + prev
            last = prev
            prev = num
        return num