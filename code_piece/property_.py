class Student:
    def __init__(self):
        self._birthday = 2000
        
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        assert value > 1980, "birthday must be larger than 1980"
        self._birthday = value
        
    @property
    def age(self):
        return 2018 - self._birthday
    
    
Jack = Student()
print(Jack.birthday, Jack.age)
Jack.birthday = 2001
print(Jack.birthday, Jack.age)
Jack.birthday = 1900 # AssertionError: birthday must be larger than 1980
Jack.age = 10 # AttributeError: can't set attribute

