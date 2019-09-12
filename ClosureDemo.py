"""
Closure

A closure is a function where every free variable, everything except parameters,
used in that function is bound to a specific value defined in the enclosing scope of that function.
In effect, closures define the environment in which they run, and so can be called from anywhere.

The concepts of lambdas and closures are not necessarily related,
although lambda functions can be closures in the same way that normal functions can also be closures.
Some languages have special constructs for closure or lambda (for example, Groovy with an anonymous block of code as Closure object),
or a lambda expression (for example, Java Lambda expression with a limited option for closure).

Here’s a closure constructed with a normal Python function:
"""

print("Closure done with normal function")

def outer_func(x):
    y = 4

    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")

        return x + y + z

    return inner_func  # return a function to parent func


for i in range(3):
    closure = outer_func(i)  # inner func exposed to outside, it's like a tail on top of the head, a circle.

    print(f"closure({i + 5}) = {closure(i + 5)}")

"""
outer_func() returns inner_func(), a nested function that computes the sum of three arguments:

    x is passed as an argument to outer_func().
    y is a variable local to outer_func().
    z is an argument passed to inner_func().

To test the behavior of outer_func() and inner_func(), outer_func() is invoked three times in a for loop that prints the following:



On line 9 of the code, inner_func() returned by the invocation of outer_func() is bound to the name closure. 
On line 5, inner_func() captures x and y because it has access to its embedding environment, such that upon invocation of the closure, 
it is able to operate on the two free variables x and y.

Similarly, a lambda can also be a closure. Here’s the same example with a Python lambda function:


"""
print("Closure done with lambda expression")

def outer_func2(x: int):
    y = 4
    return lambda z: x + y + z

for i in range(4):
    closure2 = outer_func2(i)
    print(f"closure({i,i+5}) = {closure(i+5)}")


# final conclusion: closure is a parent function returned its nested function as a callback function