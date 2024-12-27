def is_prime(func):

    def wrapper(*args, **kwargs):
        result2 = func(*args, **kwargs)
        if result2 < 2:
            print("Составное")
            return result

        for i in range(2, int(result2**0.5) + 1):
            if result2 % i == 0:
                print("Составное")
                return result2
        print("Простое")
        return result2

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)