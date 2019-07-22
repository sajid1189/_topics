import time
import math

from iterators import my_range
from decorators import time_logger


@time_logger
def lazy(size):
    result = map(math.sqrt, my_range(size))
    for i in result:
        print(i)
        time.sleep(.1)

d = lazy.__module__
print(d)
lazy(2)
