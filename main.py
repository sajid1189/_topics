from iterators import *


if __name__ == '__main__':
    # my_range = MyRange(5, 10)
    # print(next(my_range))
    # print(next(my_range))
    # print(next(my_range))
    #
    # for val in my_range:  # should start from 8
    #     print('in loop', val)
    # my_range2 = MyRange(100)
    # for val in my_range2:
    #     pass
    # print('more', next(my_range2)) # -> Should throw StopIteration exception
    # my_range3 = MyRange() -> Should throw Value error

    r = my_range(10)
    print(next(r))
    print(next(r))
    for i in r:  # should start from 3
        print('in loop', i)
