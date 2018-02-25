def args_func(*args):
    for arg in args:
        print(arg)

def kargs_func(**kargs):
    for k, v in kargs.items():
        print("{}, {}".format(k, v))
        
args_func(1,2,3,4,5)
kargs_func(k1=1, k2=2, k3=3, k4=4, k5=5)
