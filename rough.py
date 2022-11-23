import copy
import time

str_time = time.perf_counter()


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


num = 110
print("Factorial of", num, "is", )
get_re = fact(num)
end_time = time.perf_counter()
print(end_time-str_time)

str_1time = time.perf_counter()
ver = copy.copy(get_re)
end1_time = time.perf_counter()
print(end1_time-str_1time)


