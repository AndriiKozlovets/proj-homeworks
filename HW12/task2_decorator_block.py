def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function:\
 {type(e).__name__} {str(e)}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


# Calling a function
some_function_with_risky_operation({'foo': 'bar'})
# Result: Found 1 error during execution of your function: KeyError 'key'

some_function_with_risky_operation({'key': 'bar'})
# Result: bar
