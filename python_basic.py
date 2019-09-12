# --Ask for help
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
print(a_set) # {1, 2, 3, 4}
b_set = set("mingxingsu")
print( a_set & b_set)
print( a_set | b_set)
print( a_set - b_set)
print( a_set ^ b_set)
a_set.add(9)
b_set.remove('i')
a_set.update([6,7,8])
5 in a_set
'n' not in b_set
a_set.issubset(b_set)
b_set.issuperset(a_set)
new_set = a_set.copy()
b_set.discard('g')
print(b_set)

set_expre = {x**2 for x in range(4)}
print(set_expre)


# frozenset: not support add and remove, thus it can be used as key of dict
fs1 = frozenset(a_set)
dict1 = dict()
dict1[fs1] = 9
print(dict1)


# bool type
type(True) # bool
isinstance(True,int) # True
False == 0 # True
True is 1 #false


# dynamic type

# type is object, not variable, every type will contain type identifier and reference count
L = [1]
M = [1]
print( L is M) # False

# Reference shared
L = M = [1]
print( L is M) # True

# enhanced assignment
L = M = [1, 2]
L = L + [3, 4]
print(L) # L was created in  new list
print(M) # M not affected

L = M = [1, 2]
M += [3, 4] # L +=[3, 4] will be the same
print(L)
print(M)

# common string const and string expression

S = '' # backspace
S = 'Hello'
S1 = "Hello" # double quota the same as single quota
repr(S)
repr(S1)

S= r'\@temp$%123;' # raw string, no change the meaning of string
print(S)
S= u'this is unicode string'
print(S)
B=b'hello' # bytes string, saved as integers
print(B)
print(B[0]) # 104

# str to bytes : S.encode()
# bytes to str: decode
print(S.encode("utf-8"))
print(B.decode(encoding='ascii'))

# another way to decode/encode
str(B, encoding='ascii')
bytes(S, encoding='ascii')

import sys,locale
print(sys.getdefaultencoding())
print(locale.getpreferredencoding())

hs = 'hello'
ws = 'world'
print(hs+ws)
print(hs*3) # duplicate times
print(ws[1:2])
print(len(hs))

# string format
hsf = 'a %s apple' % 'red' # %s placeholder, % following the variable
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
sstr.capitalize() # first letter capitalized
sstr.title() # first letter capitalized of every word
sstr.isalnum()
sstr.isalpha()
sstr.isdigit()
sstr.islower()
ntest1= '123'
print(ntest1.isnumeric())
print(ntest1.isalnum())
print(sstr.ljust(50))
print(sstr.rjust(50))
print(sstr.center(50))
print(sstr.replace('a', 'aaa'))

#zero fill
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
print(chr(chrInt1)) #a
ordStr1 = 'a'
print(ord(ordStr1)) # 97

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
       "world" # this will be considered as one line

print(name)
print("this is %d  %s bird" % (1, 'dead')) # position
print("%s---%s---%s" % (123, 1.23, [1,2,3]))
alignA = 1234
print("%d...%6d...%-6d...%06d" % (alignA, alignA, alignA, alignA)) #ljust, rjust, zfill
alignA=1.23456789
print("%e|%f |%g" % (alignA, alignA, alignA))
print('%6.2f--%-6.2f--%06.2f--%+6.2f' % (alignA, alignA, alignA, alignA)) # +6.2f force to display sign
print("first name = %(first)s, last name = %(last)s" % {"first" : "mingxing" , "last":"su"})

print("%(myList)s" % vars()) # return a dict which contains all variables in current function


# string format 2

# based on position

# based on key

# based key and position mixed
print("I have {0} daughters,  their names are  {1[name]}".format(2, {'name' : 'jessica and sofie'}))
print("I have {0} daughters,  their names are  {dict1[name]}".format(2, dict1 = {'name' : 'jessica and sofie'}))

# based on key's properties, offset of position
import sys
print("{sys.platform} is the platform ".format(sys=sys))

# based on position's key and properties

# based on format pattern  "{fieldname:format_sepc}".format()
    # fieldname:a number or key, following selectable members or ['index']
    # format_sepc
print("{0:0^+10.2f}, {1:0<8.4f}".format(1.2345789, 3.1415)) # position : fill, align,sign, width, '.', precision, type
print("My name is {0:>{1}}.".format('Max', 20))

# List operations
L = [[1, 2, 3], 'hello', {}] # nested list
L = list('hello') # ['h', 'e', 'l', 'l', 'o']
L = list(range(4, 10))
#L = list(map(ord, 'hello'))
len(L)
L.count(1)
L.append(99) # to be appended element type can be different from exist list's element type
L.insert(0, 'c')
L.extend('D') # same element type
L.pop()
print(L.pop(5)) # return element at index, and remove it from the list, default is to remove the last one
L.extend('c')
L.remove('c') # remove the first found object
L.reverse()

# remove some consistent elements with slice
L[1: 3]=[]

L = list(range(10))
del L[::2]
print(L)

























