import time


def rate_limiter(limit, interval):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            now = time.time()
            call_times.append(now)
            # Delete calls that are no longer included in the interval
            while call_times and call_times[0] < now - interval:
                call_times.pop(0)
            if len(call_times) <= limit:
                return func(*args, **kwargs)
            else:
                raise Exception(f"Rate limit exceeded.\
 Max {limit} calls per {interval} seconds.")
        return wrapper
    return decorator


# Example usage
@rate_limiter(limit=3, interval=60)  # Max 3 calls per minute
def my_function():
    print("Function executed")


# Call the function 3 times within 60 seconds
for i in range(3):
    my_function()
    time.sleep(3)  # Wait 3 seconds between calls

# Call the function 4 times
try:
    my_function()
except Exception as e:
    print(e)  # Message about exceeding the limit
