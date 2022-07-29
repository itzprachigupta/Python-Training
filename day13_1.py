from operator import truediv
from threading import *
import time
def f1(n):
    for x in range (n):
        time.sleep(2)
        print(current_thread().name,x)
start=time.time()
t1=Thread(target=f1,args=[5],name='Thread1')

def f2():
    for x in range (6,10):
        time.sleep(1)
        print(current_thread().name,x)
t2=Thread(target=f2,name='Thread2')

def f3():
    while True:
        print('hello')
t1.start()
t2.start()
t1.join()
t3=Thread(target=f3,name='Thread3',daemon=True)
t3.start()
print(t3.isDaemon())
print(current_thread().name)
end=time.time()
print('time taken',end-start)
