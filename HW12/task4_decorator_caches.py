def cache_result(func):
    cache = {}  # Dictionary to store cached results

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


# Example usage
@cache_result
def add(a, b):
    print(f"Calculating {a} + {b}")
    return a + b


result1 = add(1, 2)
print(result1)

result2 = add(1, 2)
print(result2)
