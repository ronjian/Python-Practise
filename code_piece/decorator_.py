import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper():
        print("is going to call {} ".format(func.__name__))
        print(func.__doc__)
        print("the module of the func is {}".format(my_func.__module__))
        start_time = time.clock()
        func()
        end_time = time.clock()
        print("cost time is {}".format(start_time - end_time) )  
    return wrapper

@timeit
def my_func():
    """
    here is my_func doc.
    """
    print("in my_func")
    
# my_func = timeit(my_func)
my_func()