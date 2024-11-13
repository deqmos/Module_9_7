def is_prime(func):
    def prime(n):
        return n > 1 and all(n % j != 0 for j in range(2, int(n ** 0.5) + 1))

    def wrapper(*args, **kwargs):
        if prime(func(*args, **kwargs)):
            return "Простое"
        else:
            return "Составное"

    return wrapper


@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result2 = sum_three(1, 2, 3)
print(result2)
