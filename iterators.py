class MyRange:

    value = 0

    def __init__(self, *args):
        self.start = 1
        if len(args) == 2:
            self.start = args[0]
            self.end = args[1]
        elif len(args) == 1:
            self.end = args[0]
        else:
            raise ValueError("At least one argument is expected")
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(*args):
    start = 1
    if len(args) == 2:
        start = args[0]
        end = args[1]
    elif len(args) == 1:
        end = args[0]
    else:
        raise ValueError("At least one argument is expected")

    while True:
        if start > end:
            raise StopIteration
        yield start
        start += 1


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
