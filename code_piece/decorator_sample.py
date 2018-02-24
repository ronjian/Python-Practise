import time

def timeit(func):
    def wrapper():
        start_time = time.clock()
        func()
        end_time = time.clock()
        print("cost time is {}".format(start_time - end_time) )  
    return wrapper

@timeit
def my_func():
    print("in my_func")
    
# my_func = timeit(my_func)
my_func()