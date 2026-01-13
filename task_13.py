import time

def cached(max_size: None, seconds: int):
    def decorator(func):
        cache = {}
        order = []

        def wrapper(x):
            current_time = time.time()

            if x in cache:
                result, timestamp = cache[x]
                if current_time - timestamp < seconds:
                    return result
                else:
                    del cache[x]
                    order.remove(x)

            result = func(x)
            cache[x] = (result, current_time)
            order.append(x)

            if len(order) > max_size:
                oldest = order.pop(0)
                del cache[oldest]
            
            return result
    
        return wrapper
    return decorator


@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print(slow_function(2))
print(slow_function(2))
time.sleep(15)  
print(slow_function(2))