# --Ask for help
from filecmp import cmp
from functools import reduce
from importlib import reload
from multiprocessing import process

myList = []
myObj = {}
dir(myObj)  # --return all methods of object, and return a string list
help(myList.append)  # show function usages

# check instance type
if isinstance(myList, list):
    print("myList is a list")
myInt = 1;
if isinstance(myInt, int):
    print("myInt is an integer")

# --python types
# Hash-able types, can be key of dict
# int, float, decimal.Decimal, faction.Fraction, complex
# str, bytes
# tuple
# frozenset
# True, False
# None

# Non Hash-able: list, dict, set

# numbers const

1234, -123, 0, 9999999

1.23, 3.14e-10, 4E210, 4.0e+21
print(3.14e-3)  # 0.00314
print(4e+10)  # 40000000000.0
print(4.0e+5)  # 400000.0

print(0o123)  # oct
print(0x9AF)  # hex
print(0X9AB)  # hex
print(0b110011)  # binary

# complex
print(3 + 4j)
myInt = 65
print(hex(myInt))
print(oct(myInt))
print(bin(myInt))

# change string to int , base is rank
"string to int:"
int("123")
int("123", 10)
int("12F", 16)
int("123", 8)
int("101", 2)

# long integer : end with l/L

# infinite, negative infinite, non-number
float('inf')
float('-inf')
float('nan')

# yield : return iterator of iterable object
myList = [x * x for x in range(5)]

# create an iterator
myIterator = (x * x for x in range(5))
for i in myIterator:
    print(i)


def createIterator():
    for x in range(4):
        yield x * x


for x in createIterator():
    print(x)

# lambda expression
# lambda args : expression
lambda x: x + 1
addOne = lambda x: x + 1
addOne(2)

print((lambda x: x * x)(5))

full_name = lambda first, last: f'full name is : {first.title()}, {last.title()}'
print(full_name('Mingxing', 'max su'))

# higher-order functions: pass func to func
high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
high_ord_func(2, lambda x: x + 3)

(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1, 2, 3)
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

x = 0
y = 1
z = 2
print(x == 1 if y else z)

# conditional expression
# [on_true] if [expression] else [on_false]
a, b = 10, 20
print(" a less than b " if a < b else "a greater than b" if a > b else "a equals to b")
a, b = 10, 10
print(" a less than b " if a < b else "a greater than b" if a > b else "a equals to b")

# not in :
# is , is not

if 1 < a < 20:
    print(" a between 1, 20")

# slice(start, stop, increment),
a = [1, 2, 3, 4, 5, 6]
b = a[2:4:1]
c = a[::-1]  # reverse
d = a[:5:2]

t = (1, 2, 3, 4, 5, 6)
t1 = t[1:4]
print(t1)

# type cast
tCastVar1 = int(3.1415)
print(tCastVar1)

# in , not in

print(3 in [1, 2, 3])
print('a' not in ('b', 'c'))

# is , is not

'''

Exponentiation (raise to the power)
 **


Complement, unary plus and minus (method names for the last two are +@ and -@)
~ + -



Multiply, divide, modulo and floor division
* / % // 	



Addition and subtraction
+ - 	



Right and left bitwise shift
>> << 	



Bitwise 'AND',Bitwise exclusive `OR' and regular `OR'
&,^,| 	


Comparison operators
<= < > >= 	

Equality operators
<> == != 	



Assignment operators
= %= /= //= -= += *= **= 	


Identity operators
is is not 	


Membership operators
in not in 	


Logical operators
not or and

'''

# floor division/integer division, result with faction removed.
print(5.0 / 2)  # 2.5
print(5.0 // 2)  # 2

# integer.bit_length()
bt1 = 1
bt2 = 1024
print(bt1.bit_length())
print(bt2.bit_length())

# str: for readable
# repr : for development, construct object, all information
print(repr(myList))
print(repr("this is from str"))
print(str("this is from str"))

# decimals
import decimal
from decimal import Decimal

decimal.getcontext().prec = 4

print(Decimal("0.01") + Decimal("0.02"))
print(str(Decimal(22 / 7))[:6])

x = 13.9401249999999999999999
x_str = "{0:.2f}".format(x)
x_float = float(x_str)
print(x_float)
print(round(x, 2))

# fraction
from fractions import Fraction

x_fraction = Fraction(4, 6)
y_fraction = Fraction("0.25")
print(x_fraction)
print(y_fraction)

# set: unordered, element unique collection
#  support operations: union, intersection, difference, symmetric difference, in set, len(set), for x in set
a_set = set([1, 2, 3, 4])
print(a_set)  # {1, 2, 3, 4}
b_set = set("mingxingsu")
print(a_set & b_set)
print(a_set | b_set)
print(a_set - b_set)
print(a_set ^ b_set)
a_set.add(9)
b_set.remove('i')
a_set.update([6, 7, 8])
5 in a_set
'n' not in b_set
a_set.issubset(b_set)
b_set.issuperset(a_set)
new_set = a_set.copy()
b_set.discard('g')
print(b_set)

set_expre = {x ** 2 for x in range(4)}
print(set_expre)

# frozenset: not support add and remove, thus it can be used as key of dict
fs1 = frozenset(a_set)
dict1 = dict()
dict1[fs1] = 9
print(dict1)

# bool type
type(True)  # bool
isinstance(True, int)  # True
False == 0  # True
True is 1  # false

# dynamic type

# type is object, not variable, every type will contain type identifier and reference count
L = [1]
M = [1]
print(L is M)  # False

# Reference shared
L = M = [1]
print(L is M)  # True

# enhanced assignment
L = M = [1, 2]
L = L + [3, 4]
print(L)  # L was created in  new list
print(M)  # M not affected

L = M = [1, 2]
M += [3, 4]  # L +=[3, 4] will be the same
print(L)
print(M)

# common string const and string expression

S = ''  # backspace
S = 'Hello'
S1 = "Hello"  # double quota the same as single quota
repr(S)
repr(S1)

S = r'\@temp$%123;'  # raw string, no change the meaning of string
print(S)
S = u'this is unicode string'
print(S)
B = b'hello'  # bytes string, saved as integers
print(B)
print(B[0])  # 104

# str to bytes : S.encode()
# bytes to str: decode
print(S.encode("utf-8"))
print(B.decode(encoding='ascii'))

# another way to decode/encode
str(B, encoding='ascii')
bytes(S, encoding='ascii')

import sys, locale

print(sys.getdefaultencoding())
print(locale.getpreferredencoding())

hs = 'hello'
ws = 'world'
print(hs + ws)
print(hs * 3)  # duplicate times
print(ws[1:2])
print(len(hs))

# string format
hsf = 'a %s apple' % 'red'  # %s placeholder, % following the variable
print(hsf)

hsf2 = ' these are  {0} {1} apples '.format(2, 'red')
print(hsf2)

# join strings
print('|'.join(['hello', 'world', 'nihao']))

# builtin string functions
sstr = '  a This Is a String bb  '
sstr.upper()
sstr.lower()
sstr.swapcase()
sstr.capitalize()  # first letter capitalized
sstr.title()  # first letter capitalized of every word
sstr.isalnum()
sstr.isalpha()
sstr.isdigit()
sstr.islower()
ntest1 = '123'
print(ntest1.isnumeric())
print(ntest1.isalnum())
print(sstr.ljust(50))
print(sstr.rjust(50))
print(sstr.center(50))
print(sstr.replace('a', 'aaa'))

# zero fill
print(print(sstr.zfill(50)))

print(sstr.rfind('in'))
print(sstr.lower().count('i'))
print(len(sstr.strip()))
print(len(sstr.lstrip()))
print(sstr.rstrip())
print(sstr.rstrip().rstrip('b'))
print(sstr.lstrip().lstrip('a'))

# string cast
int('42')
str(42)
float(3.14)
float('3.14')
str(3.14)

# help(ord) # ord(c, /)     Return the Unicode code point for a one-character string.

# help(chr)  chr(i, /)      Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
chrInt1 = 97
print(chr(chrInt1))  # a
ordStr1 = 'a'
print(ord(ordStr1))  # 97

# cast any base number string to int
print(int(b'0x9ff', 16))
print(int('9ff', 16))
print(int('1001', 2))

# cast int to any base number string
print(hex(2559))
print(bin(9))
print(oct(64))

# string contactation special
name = "hello" "world"
print(name)

name = "hello" \
       "second line" \
       "world"  # this will be considered as one line

print(name)
print("this is %d  %s bird" % (1, 'dead'))  # position
print("%s---%s---%s" % (123, 1.23, [1, 2, 3]))
alignA = 1234
print("%d...%6d...%-6d...%06d" % (alignA, alignA, alignA, alignA))  # ljust, rjust, zfill
alignA = 1.23456789
print("%e|%f |%g" % (alignA, alignA, alignA))
print('%6.2f--%-6.2f--%06.2f--%+6.2f' % (alignA, alignA, alignA, alignA))  # +6.2f force to display sign
print("first name = %(first)s, last name = %(last)s" % {"first": "mingxing", "last": "su"})

print("%(myList)s" % vars())  # return a dict which contains all variables in current function

# string format 2

# based on position

# based on key

# based key and position mixed
print("I have {0} daughters,  their names are  {1[name]}".format(2, {'name': 'jessica and sofie'}))
print("I have {0} daughters,  their names are  {dict1[name]}".format(2, dict1={'name': 'jessica and sofie'}))

# based on key's properties, offset of position
import sys

print("{sys.platform} is the platform ".format(sys=sys))

# based on position's key and properties

# based on format pattern  "{fieldname:format_sepc}".format()
# fieldname:a number or key, following selectable members or ['index']
# format_sepc
print("{0:0^+10.2f}, {1:0<8.4f}".format(1.2345789, 3.1415))  # position : fill, align,sign, width, '.', precision, type
print("My name is {0:>{1}}.".format('Max', 20))

# List operations
L = [[1, 2, 3], 'hello', {}]  # nested list
L = list('hello')  # ['h', 'e', 'l', 'l', 'o']
L = list(range(4, 10))
# L = list(map(ord, 'hello'))
len(L)
L.count(1)
L.append(99)  # to be appended element type can be different from exist list's element type
L.insert(0, 'c')
L.extend('D')  # same element type
L.pop()
print(L.pop(5))  # return element at index, and remove it from the list, default is to remove the last one
L.extend('c')
L.remove('c')  # remove the first found object
L.reverse()

# remove some consistent elements with slice
L[1: 3] = []

L = list(range(10))
del L[::2]
print(L)

# -----------------Dictionary-----------
D = {}
D = {'name': 'max', 'details': {'ID': '9527', 'email': '123@gmail.com'}}
D = dict.fromkeys(['key1', 'key2'], 'default value')
D = dict(name='tom', age=12)  # init from *kargs
D = dict([('name', 'tom'), ('age', 12)])  # from iterable tuples
D = dict(zip(['name', 'age'], ['tom', 12]))
D["lucy"] = 12
vLucy = D.get("lucy", 10)
print(D)
print(D.keys())
print(D.values())
print(D.items())
print(vLucy)

D2 = dict(name='ming', age=20)
D.update(D2)
print(D)

D.setdefault('ming', 30)
print(D.pop('max', 20))
# del D


if 'max' not in D:
    D['max'] = 34
if 'ming' in D:
    D.pop('ming')

D = {k: 1 for k in ['key1', 'key2']}
D = {k: v for (k, v) in zip(['name', ' age'], ['Max', 22])}
print(D)


class Dict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


dct = dict()
dct.get("foo", "123")

# tuple is const, no matter where it is
a = [(1, 2)]
# a[0][1]=2 #'tuple' object does not support item assignment

a = (1)  # now a is an integer
print(type(a))
a = (1,)  # now a is a tuple
print(type(a))

# -----------------file operations------------
path = r'/home/jessiesofie0720/Documents/test/hello.txt'
with open(path, 'w') as fs1:  # supports : w, r, a, wb, rb, ab : binary mode is for Windows (JPEG, EXE files)
    fs1.writable()
    fs1.write('a')  # without \n
    fs1.writelines("hello from python\n123")
    fs1.flush()

for line in open(path):  # better to use this one to read big size file
    print(line)

with open(path, 'r') as fs1:  # with is like using in c#, can make sure file closed after operation finished.
    fs1.readline(1024)
    fs1.readable()
    fs1.readlines()
    print(fs1.isatty())
    print(fs1.fileno())  # file signature, long int
    print(fs1.tell())  # get offset postion
    print(fs1.seekable())

    fs1.close()

# open('f.bin', 'rb') # read binary file
# open('f.txt', encoding='latin-1')


# Number is 0 -- false, Number is non-0, True
# Other objects : non-None: True

'''----------------------------------grammar and sentences---------------------'''

# Assignments
foo = 'boo'
foo, bar = 'foo', 'bar'
[foo, bar] = ['foo2', 'bar2']
a1, b1, c1, d1 = 'abcd'
print(d1)  # a, b, c, d

a, *b, c = 'foo'
print(type(b))
print(a, b, c)

foo = bar = '|foobar'  # shared reference
print(foo is bar)

foo += ' enhanced'
print(foo, bar)

[a, b, c] = (1, 2, 3)  # a=1, b =2 c = 3
a, b, c = range(3)  # a=1, b =2 c = 3
a, *b = [1, 2, 3, 4]  # a= 1, b=[2,3,4]
*a, b = [1, 2, 3, 4]  # a= [1,2,3], b=4
a, *b, c = [1, 2, 3, 4]  # a= 1, b=[2,3], c= 4
# variable without * has higher priority
a, *b, c = [1, 2]  # a= 1, c = 2, b=[]

# stream redirect
print("this is from stdout")
temp = sys.stdout
sys.stdout = open(path, 'a')
print("this is from stdout redirect")
sys.stdout.close()
sys.stdout = temp  # reset to original

with open(path, 'r') as fs1:
    print(fs1.readlines())

# if/else  3 segment
print(1 or 2 or 3)  # 1
print(1 and 2 and 3)  # 3

a = 10
result = 'a greater than 10' if a > 10 else ('a greater than 5' if a > 5 else 'a greater than 0')
result = (a > 10 and 'a greater than 10' or a > 5 and 'a greater than 5' or a > 0 and 'a greater than 0')
print(result)

a = 5
# While and for loops have 'else'
while a > 1:
    print(a)
    a -= 1  # do_some_thing
else:
    print("else is being executed")
    # do some other thing, will be executed after while loop ends, unless there is break in while loop.

for i in range(5):
    print(i)
    i += 1
else:
    print("else is being executed in for loop")

# For loop to do assignment
for (a, b) in [(1, 2), (3, 4)]:
    print(str(a) + '....' + str(b))

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(c)

for ((a, b), c) in [(('A', 'B'), 'C'), ('XY', 'z')]:
    print(a + '..' + b)

for (a, *b) in [(1, 2, 3), (4, 5, 6)]:
    print(b)

M = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
resSum = [sum(m) for m in M]
print(resSum)
resSum = [c * 2 for c in 'hello']
print(resSum)

resSum = [a * b for a in [2, 3] for b in [4, 5]]
print(resSum)

resSum = [a * b for a in [2, 3] for b in [4, 5, 6] if b > 5]  # filter where
print(resSum)
resSum = [a if a > 0 else 0 for a in [-1, 0, 1]]  # filter select list
print(resSum)

# parse 2 list together: zip
for name, age in zip(['XiaoA', 'XaioB'], ['15', '16']):
    print(name, age)
# parse  with index
for index, name in enumerate(['XiaoA', 'XaioB', 'XiaoC']):
    print(index + 1, name)

# generator
G = (m ** 2 for m in [1, 2, 3])
print(next(G), next(G), next(G))

# parse syntax can alo used to generate set {}, and dict {a:b}
G = {m * 10 for m in [1, 2, 3]}
print(G)

G = {m: m * 10 for m in range(3)}
print(G)

"""
this is the module doc
"""


class MyClass(object):
    """
    this is class doc
    """
    print()


def MyFunc():
    """
    this is the function doc
    """
    print()


print(MyClass.__doc__)
print(MyFunc.__doc__)

# variable name conventions
#  _X, will not be imported by 'from module import *'
#  __X__. system variable, special meaning to interpreter
#  __X, private local variables


print(sorted(iter([9, 8, 5, 2, 3, 1])))
print(map(str.upper, 'hello'))
print(list(map(str.upper, 'hello')))
print(list(zip(['a', 'b'], [1, 2])))

# del variable
del myList

# sub list [start:stop:increas]
X = [x for x in range(5)]
X[:3]  # first 3
X[1:5]  # from 1 to 4, stop at 5th
X[-3:]  # 3rd from the end, and to the end
X[::2]  # even

# iterabor
I = iter(X)
I.__next__()
print(I.__next__())

# Iterable types: range(), map(), zip(), filter(), Dict.keys(), Dict.items(), files
for i in filter(str.islower, 'HeLlo'):
    print(i)  # display all lower

"""
--------------------------function syntax --------------------------------
"""

def f():
    print('Inside f() : ', a)

# global

MyFunc()  # call a function


a = 1
# Uses global because there is no local 'a'


# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)


# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# nonlocal MyNonLocalVar = "outer scope var is used in function or other domain, like protected"
# lambda MyAnnouymousFunc


# variable parsion LEGE: Local->Enclosing->Global->Built in


# Nested function: factory functiom
def maker(N):
    def action(X):
        return X == N

    return action


f1 = maker(2)
print(f1(3))


def outer():
    a = 5

    def inner():
        nonlocal a
        a = 10

    inner()
    print(a)


outer()

# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
print("Value of a without using nonlocal is : ", end="")


def outer():
    a = 5

    def inner():
        a = 10

    inner()
    print(a)


outer()

# Summary: because python allows vars to share names in differnet scope, it has to differenciate them by using nonlocal/global

# Pass values to parameters of function

# based on postion
def f(a,b,c):print(a,b,c)
f(1,2,3)
f(1, c = 4, b = 5) # parameter keyword

# default parameter
def f2(a, b='b', c ='c'):print(a,b,c)

f2('a')
f2('a', b='bbb')
f2(a='aaa', c='cc')

#after *args parameter, keyword parameter required
import string

# collect parameters from tuples
def keywordOnly(a, *args, c): print(a, args, c) # keywordOnly(1, list1, c= defaultValueOfC)
def keywordOnly(a, *args, b, c): print(a, args , b, c) #  keywordOnly(1, list1, b=defaultValueOfB, c= defaultValueOfC)
def keywordOnly(a, *args, b, c=1): print(a, args, b, c) #  keywordOnly(1, list1, b=defaultValueOfB)

keywordOnly(1, b=[1,2], c = 5)
keywordOnly(1, 'hello','foo', 'bar', b= 5, c=3)
keywordOnly(1, 'world',' world 2',' world 3', b= 5) # result:1 ('world', ' world 2', ' world 3') 5 1

# Parse from list
def f3(*args):print(args)
f3(1,2,3)

# parse from dict
def f4(**args):print(args.keys())
f4(a=1, b=2)

# list and dict mixed
def f5(a, *list1, **dict1): print(a, list1, dict1)
f5(1, (2,3), c= 4, d=5)


def my_func(a, *b): print(a, b[1] if len(b) > 1 else b[0])
my_func(1, *(2,3)) # my_func(1,2,3)

def my_func(a, *l, **dict1): print(a, l, dict1)
my_func(1, *(2,3),** {'b':4,'c':5}) # my_func(1,2,3)


#properties

my_func.level = 2
print(my_func.level)


# function annotation in def line: to explain parameter type and  conditions, return value type, etc,
def my_func(a: 'first parameter' = 'foo', b: range(1,10) = 0, c:float = 1.0) ->int:
    print(a, b,c)
print(my_func.__annotations__)


#lambda with map (like select in LINQ), filter(like where in LINQ), reduce(like aggregate function in LINQ)
L = list(map(lambda x: x*2+10,  [1,2,3]))
print(L)
L = list(filter(lambda x: x < 0,  range(-5,5)))
print(L)
newL = reduce(lambda x, y  : x + y, range(0,9))
print(newL)

# Creator

cr = (x**2 for x in range(2))
print(0 in cr)
print(1 in cr)
print(4 in cr) # out of stream



globalX = 22
def test():
    print(globalX) # 22
    X = 88
    print(globalX) # 22

test()

def test2():
    global globalX
    globalX= 88
    print(globalX) # 88

test2()


# function's paramter's default value is initiated at definition instead of calling

def foo(nums =[]):
    nums.append(9)
    print(nums)

foo() # [9]
foo() # [9,9]
foo() # [9,9,9]

def foo(nums = None):
    if nums is None: nums=[]
    nums.append(9)
    print(nums)

foo() # [9]
foo() # [9]
foo() # [9]


########### colections opeations ##########
it =iter([1,2,3])
print(it.__next__())
print(it.__next__())

for x in enumerate([1,2,3],10):
    print(x)
max([1,2,3])
min([1,2,3])

dict2 = dict()
'''
list()
set()
frozenset()
tuple()
str()
sorted()

all() if all true, return true, if 0, return true
any() if any one is true, return true, empty return false
'''


print(cmp(1,2))


# IO operaitons
#msg = input()
# print('Hello ,' +  msg)
#open(path,'r')

isCallable: bool = callable(my_func)
print(isCallable)


myList = list([1,2,3])
mems = dir(myList)
print(mems)

#wrapper method
classmethod(f2)
staticmethod(f2)


le = eval('lambda x : x*2')
print(le(10)) # 20

str =r'print("Execute this pythong string ")'
exec(str)

#execfile: exec(open('./filename').read())

print(hasattr(myList, 'count'))
print(getattr(myList, 'count'))

def MyAttFunc():
    a = 1

setattr(MyAttFunc, 'a', '9')

print(MyAttFunc.a)

delattr(MyAttFunc,'a')
#print(getattr(MyAttFunc, 'a')) # no attribute any more

#globals() # return all global vars as a dic
# locals()

#hash()
print(hash(my_func))

print(id(my_func))

print(isinstance(1,int))

class A:
    print('in class A')
    def showFlag(self):
        print('in function of class A')

class B(A):
    print('in class B')
    def showFlagBversion(self):
        print('in function of class B')

    def printLocals(self):
        a= 1
        b= 2
        c= 'hello'
        print(locals())

B().showFlagBversion()
B().showFlag()
print(issubclass(B, A))
B().printLocals()

reload(sys)

print(vars(A))

print(zip([1,2,3],['a','b','c']))
print(list(zip([1,2,3],['a','b','c'])))


# -----------------------------------------Modules------------------
# module search path: executing path- > PYTHONPATH -> Standard linkable libs path- > *.pth file content

import sys
sys.path
sys.argv # arguments of python script
sys.platform
sys.modules # loaded modules
sys.stdout
sys.stderr
sys.stdin
print(sys.modules)


# import modules
import sys, importlib # import module name
from importlib import reload # from module name, import member name

# import package of module with '.'
# import dir1.dir2.module1
# from dir1.dir2.module1  import *

#import from relative path

# from .string import *
# from . import foo # from current path, instead of  sys path

# __all__ = ['x1','x2', 'x3'] # import all list
# _X will not  be included in the import all. Underscore as a surffix
# from .ImportScopeTest import *
#print(varImportScopeTest)
print(__name__)
print(__doc__)
print(__file__)
print(__package__)



# ----------------Exceptions----------------------------
# with/as <=> try cathch finally


'''
 try statement works as follows.

    First, the try clause (the statement(s) between the try and except keywords) is executed.

    If no exception occurs, the except clause is skipped and execution of the try statement is finished.

    If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.

    If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

'''
#capture
def DemoCaptureException():
    try:
        b = 1 / 0
    except ZeroDivisionError as zeroDiv: # 'as' follows the instance of exception.
        print(zeroDiv.args)
        print(type(zeroDiv))
    except (RuntimeError, TypeError, NameError): # One line can capture multiple exceptions, at the most one to be triggered
        pass


DemoCaptureException()

# user defined expcetion
class MyError(Exception):
    pass


class InputError(MyError):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(MyError):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next


'''
    If a finally clause is present, the finally clause will execute as the last task before the try statement completes. 
    The finally clause runs whether or not the try statement produces an exception. 
    The following points discuss more complex cases when an exception occurs:

    If an exception occurs during execution of the try clause, the exception may be handled by an except clause.
     In all cases, the exception is re-raised after the finally clause has been executed.

    An exception could occur during execution of an except or else clause. Again, t
    he exception is re-raised after the finally clause has been executed.

    If the try statement reaches a break, continue or return statement, 
    the finally clause will execute just prior to the break, continue or return statement’s execution.

    If a finally clause includes a return statement, the finally clause’s return statement will execute before, 
    and instead of, the return statement in a try clause.
'''

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
        #raise ValueError('value error')
    finally:
        print("executing finally clause")

divide(2,1)
divide(2,0)
#divide('a','b') #TypeError: unsupported operand type(s) for /: 'str' and 'str'


#raise <=> throw

# raise : raise the most recent expcetion
# raise <class>
# raise <instance>



# characters encoding
# ascii  : 0~ 127,

print(ord('a'))
print(chr(100))

bytearray # mutable bytes list
bytes # imutable bytes list

#encode: string to bytes, <==> bytes(str1, encoding='')
myStr = "Hello"
bStr = myStr.encode()
print(bStr)
print(type(bStr))

#decode: bytes to string, <==> str(bytes, encoding='')
recoverStr = bStr.decode()
print(recoverStr)
print(type(recoverStr))

#bytes object
B = b'abc'
B = bytes('abc',encoding='ascii')
B = bytes([97,98,99])
B = bytes([x for x in range(97, 100)])
B = 'abc'.encode()


# array multiple dimension
lists = [0]*3
lists = [[]]*3
lists[0].append(3) # [[3], [3], [3]], shadow copy
lists = [[] for i in range(3)]

lists[0].append(3)
lists[1].append(6)
lists[2].append(9)

lists2  = [lists for i in range(4)] #3 columns, 4 rows
print(lists2)













