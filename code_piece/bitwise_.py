# https://wiki.python.org/moin/BitwiseOperators

def bin_wrapper(func):
    def wrapper(*args, **kargs):
        res = func(*args, **kargs)
        return(bin(res))
    return wrapper

@bin_wrapper
def left_shift(x, y): return x << y

@bin_wrapper
def right_shift(x, y): return x >> y

@bin_wrapper
def and_op(a, b): return a & b

@bin_wrapper
def or_op(a, b): return a | b

@bin_wrapper
def reverse(x): return ~x

@bin_wrapper
def xor(*args):
    res = None
    for arg in args:
        if res == None:
            res = arg
        else:
            res = res ^ arg
    return res

if __name__ == "__main__":
    a = 10
    b = 12
    y = 3
    print("binary of a is : {}".format(bin(a)))
    print("binary of b is : {}".format(bin(b)))
    print("a left shift {} bits is : {}".format(y, left_shift(a, y)))
    print("a right shift {} bits is : {}".format(y, right_shift(a, y)))
    print("a and b is : {}".format(and_op(a, b)))
    print("a or b is : {}".format(or_op(a, b)))
    print("reverse a is : {}".format(reverse(a)))
    print("a xor b is : {}".format(xor(a, b)))
    print("a xor a xor a is {}".format(xor(a, a, a)))
    print("a xor a xor b is {}".format(xor(a, a, b)))
