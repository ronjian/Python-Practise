class Foo(object):
    def __eq__(self, other):
        print("in __eq__ func")
        return True

ins = Foo()
print(ins is None)
print(ins == None)
