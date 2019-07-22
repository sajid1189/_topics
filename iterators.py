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
            break
        yield start
        start += 1

