"""

This module demonstrates the concept of closures with code snippet examples.

"""


def outer_func():
    x = 1

    def inner_func():
        print("value of x is", x)

    return inner_func


outer = outer_func()

# outer variable is assigned a 'callable'. This 'callable' is prepared using the variable x, which is outside
# inner_function. Even after the execution of the outer function was finished (after the statement outer = outer_func())
# But the inner function still holds the access to the variable x. And When we call the 'callable' in the following line
# it should print the value of x

outer()
# should print the following
# value of x is 1


def outer_with_param(x):

    def inner_func():
        print('value of x is', x)

    return inner_func

# outer_1 = outer_with_param(1)
# outer_1()
#
# outer_2 = outer_with_param(2)
# outer_2()

