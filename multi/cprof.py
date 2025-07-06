import cProfile
import time

def slow_func():
    return sum(i * i for i in range(1000000))

s = time.time()
print(slow_func())
print(f"total elapsed time: {time.time() - s:.2f} sec")
print(type(slow_func()))

#cProfile.run("slow_func()")