class myClass:
    vara = 123
    def __init__(self, para):
        self.para = para
        print("initialized, instance parameter is {}".format(self.para))
        
    def normal_func(self):
        print("in normal method, instance parameter is {}".format(self.para))
        
    @classmethod
    def class_func(cls):
        print("in class method, class parameter is {}".format(cls.vara))
        
    @staticmethod
    def static_func():
        print("in static method")

ins = myClass("abc")
ins.normal_func()
myClass.class_func()
myClass.static_func()
