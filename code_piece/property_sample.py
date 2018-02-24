class myClass:
    def __init__(self):
        self._vara = 0
    
    @property
    def vara(self):
        return self._vara

    @vara.setter
    def vara(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be integer")
        if value < 0 or value > 200:
            raise ValueError("value must be between 0 and 200")
        self._vara = value

class myClass_explain:
    def __init__(self):
        self._vara = 0
    
    def getter(self):
        return self._vara

    def setter(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be integer")
        if value < 0 or value > 200:
            raise ValueError("value must be between 0 and 200")
        self._vara = value
    
    vara = property(getter, setter)
        
myInstance = myClass()
print(myInstance.vara)
myInstance.vara = 100
print(myInstance.vara)

myInstance2 = myClass_explain()
print(myInstance2.vara)
myInstance2.vara = 100
print(myInstance2.vara)