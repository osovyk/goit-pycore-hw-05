def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if type(n) is not int:
            raise TypeError("The input must be integer")

        if n < 0:
            raise ValueError("Input must be positive integer")
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
