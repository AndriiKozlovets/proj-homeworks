def check_types(func):
    def wrapper(*args, **kwargs):
        # Get information about annotations of arguments
        params = func.__annotations__
        for arg_name, arg_value in zip(params.keys(), args):
            # Сheck whether the type of the argument to the annotation
            if (arg_name in params and
                    not isinstance(arg_value, params[arg_name])):
                raise TypeError(f"TypeError: Argument {arg_name}\
 must be {params[arg_name].__name__}, not {type(arg_value).__name__}")
        return func(*args, **kwargs)
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


# Calling a function
result1 = add(1, 2)
print(result1)
# Result: 3

try:
    result2 = add("1", "2")
except TypeError as e:
    print(e)
# Result: Argument a must be int, not str
