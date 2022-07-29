from threading import *
import time

def f1(n):
    for x in range (n):
        time.sleep(2)
        print(x)
start=time.time()

def f2():
    for x in range (6,10):
        time.sleep(1)
        print(x)
f1(5)
f2()
print(current_thread().name)
end=time.time()
print('time taken',end-start)
