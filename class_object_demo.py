class C2():
    print('parent class C2')


class C1(C2):
    age = 42

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name + ' :instance of C1 instance is deleted')

    def testOverload(self, input):
        print(input)

    def testOverload(self):
        print("default print in testOverload")


bob = C1('Bob')
print(bob.age)

# in python, no method overload based on parameters of method , functions with the same name will be replaced by last one
bob.testOverload()


# bob.testOverload("hello") : TypeError: testOverload() takes 1 positional argument but 2 were given

class Person():
    def __init__(self, name):
        self.name = name
        self.title = 'no title'

    def SayName(self):
        print("I am : " + self.name + " : title: " + self.title)


class Manager(Person):
    title = 'manager'  # properties belong to class instead of instance, if vars share same name with properties of class, the latter will be replaced.
    company = 'Google'

    def SayName(self):
        Person.SayName(self)  # call super method
        print("My title is a " + self.title + ' in ' + self.company
              )


personBob = Person("Bob")
managerTom = Manager("Tom")
personBob.SayName()
managerTom.SayName()  # call method : instance.method(args)
Manager.SayName(managerTom)  # Another way to call methods: , Class.method(instance, args)

personBob.__class__.__name__
personBob.__dict__

managerTom.__class__

managerTom.__dict__
Manager.__dict__

# abstract methods definitions


from abc import abstractmethod


class AbClass():
    def abstractMethod(self):
        self.aciton()  # action() undefined here , will be defined in subclass

    def abstractMethod1(self):
        raise NotImplementedError(
            "action must be defined")  # undefined and rais error here , will be defined in subclass

    @abstractmethod  # use decorator to define abstract method
    def abstractMethod2(self): pass


class DerivedClass(AbClass):
    def abstractMethod(self):
        print("abstractMethod defined in DerivedClass")

    def abstractMethod1(self):
        print("abstractMethod1 defined in action")

    def abstractMethod2(self):
        print("abstractMethod2 defined in DerivedClass")


derived = DerivedClass()
derived.abstractMethod()
derived.abstractMethod1()
derived.abstractMethod2()

# ----------------------------OO inheritances -------------
isinstance(derived, AbClass)  # 'IS - A', true


# Has - A :  wrap one object into a wrapper with hook method: __getattr__()
class wrapper(object):
    def __init__(self, object):
        self.wrapped = object

    # Hook to wrap attributes of orignal object
    def __getattr__(self, attrname):
        print("Trace: " + attrname)
        return getattr(self.wrapped, attrname)


x = wrapper([1, 2, 3])
x.append(4)  # AttributeError: 'wrapper' object has no attribute 'append'
print(x.__dict__)
print(x.wrapped)


# fake private attributes: __AttrName, can be modified  outside of class by : _ClassName__AttrName

class DemoFakePriavteVarClass(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "self.name = %s" % self.__name


demoFKC = DemoFakePriavteVarClass("tom")
print(demoFKC)
demoFKC.__name = 'David'  # doesn't change the private var's value
print(demoFKC)  # self.name = tom
demoFKC._DemoFakePriavteVarClass__name = 'David'  # self.name = David
print(demoFKC)


class DemoClassInstanceMethod(object):
    def StaticClassMethod(msg):
        print(msg)

    def InstanceMethod(self, msg):
        print(msg)


DemoClassInstanceMethod.StaticClassMethod('I am from  static method')

customWrapper = DemoClassInstanceMethod().InstanceMethod  # pass method of instance to another obj, and execute it
customWrapper("I am from instance method")

print(dir(personBob))
setattr(personBob, 'cannot touch', 'but can get from getattr')  # attribute name with backspace.
print(getattr(personBob, 'cannot touch'))

# Bind properties or methods to class/instance
m = Manager("Lee")
m.age = 30


def setAge(self, age):
    self.age = age


from types import MethodType

m.setAge = MethodType(setAge, m)  # bind to instance method to obj
m.setAge(40)
print(m.age)

Manager.setAge = MethodType(setAge, Manager)  # bind class method to class, all instance can use this method
Manager.setAge(50)
print(Manager.age)
m2 = Manager('Wallace')
print(m2.age)

# Python support multiple inheritances: search from left to right, bottum to up, width first
# Class A (B,C):    pass

# If __init__ defined in subclass, and not explicitly call super class 's __init__, python will not call for you
# If __init__ NOT defined in subclass, and  python will the first super class's __init__'


# decorator: @staticmethod,@classmethod, class decorator
# staticmethod : no first implicit parameter
"""
    A static method is also a method which is bound to the class and not the object of the class.
    A static method can’t access or modify class state.
    It is present in a class because it makes sense for the method to be present in class.
"""

# class method can access class member
"""
    A class method is a method which is bound to the class and not the object of the class.
    They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.
"""

"""
    We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
    We generally use static methods to create utility functions.
"""
from datetime import date
class Person():
    def __init__(self,name, age):
        self.name=name
        self.age=age

    @staticmethod
    def isAdult(age):
        return age > 18

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


person1 = Person('Xiao A', 19)
person2 = Person.fromBirthYear('Xiao B', 1985)

print(person1.age)
print(person2.age)
print(Person.isAdult(15))



# class as decorator for function
from time import time
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        starter = time()
        self.func(*args,**kwargs)
        endtime = time()
        print("Function execution time took: {}".format(endtime- starter))

@Timer # like attribute in .NET
def do_somework(delay):
    from time import sleep
    sleep(delay)

do_somework(3)

# demo 2: PrameterCheck
class ParameterCheck:
    def __init__(self, func):
        self.func = func

    def __call__(self, *params):
        if(any(isinstance(i, str) for i in params)):
            raise TypeError("parameter can not be string")
        else:
            self.func(*params)

@ParameterCheck
def CaculateSum(*params):
    return sum(params)

print(CaculateSum(1,2,3))
# print(CaculateSum(1,'a',3))  #TypeError: parameter can not be string

#limit properties of class : __slots__
# __slots__ limits this class can only has properties in the list, apply only to current class, not for derived class,
#   save memory, can be tuple, or list.
class DemoSlotsClass:
    __slots__ =  ['name', 'age']


#property(fget, fset, fdel, doc)
class TestPropertyClass:
    def __init__(self, val):
        self._val = val
    def getVal(self):
        return self._val
    def setVal(self, val):
        self._val = val
    def delVal(self):
        del self._val
    val = property(getVal,setVal, delVal, 'Val property')

testProper = TestPropertyClass("I am the value of Val property")
print(testProper.val)
testProper.val = 'I am the new value of val'
print(testProper.val)
del testProper.val


# with decorator to define a properpty
class TestPropertyClass2:
    def __init__(self, val):
        self._val = val

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @val.deleter
    def val(self):
        del self._val

testProper2 = TestPropertyClass2("I am the Val property created by decorator way")
print(testProper2.val)
testProper2.val ='new value'
print(testProper2.val)


 # overwrite class's methods

 # __str__, __repr__ : output string
 # __itr__, next: custom iterable
 # __getitem__, __setitem__
 # __getattr__
 # __call__

class DemoOverwriteBuiltInMethodsClass():
    def __init__(self, dict):
        self.dict = dict
    def __str__(self):
        print("I am : ")
        return  super.__str__(self)

    def __getitem__(self, item):
        print("GET:" + item)
        return self.dict[item]

    def __setitem__(self, key, value):
        print("SET:" + value)
        self.dict[key] = value



m = dict()
print(DemoOverwriteBuiltInMethodsClass(m))
DemoOverwriteBuiltInMethodsClass(m)['a']= 'aaaa'
print(DemoOverwriteBuiltInMethodsClass(m)['a'])



#dynamic way to create type: class
def sayHelloTo(self, name='world'):
    print("Hello, %s" % name)

HelloClass = type('HelloClass', (object,), dict(sayHelloTo=sayHelloTo))

h = HelloClass()
h.sayHelloTo('Max')


