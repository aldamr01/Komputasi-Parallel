import random
import time
import multiprocessing

def SoalA():
    result = []
    for i in range(0,10):
        if i%2==1:
            result.append(i)
    print(result)  

def SoalB():
    result = []
    for i in range(50,60):
        if i%2==0:
            result.append(i)
    print(result)

def SoalC():
    result = []
    for i in range(0,5):
        result.append(random.randrange(100,500))
    print(result)

if __name__ == "__main__":
    worker1 = multiprocessing.Process(target=SoalA)
    worker2 = multiprocessing.Process(target=SoalB)
    worker3 = multiprocessing.Process(target=SoalC)
    worker1.start()
    worker2.start()
    worker3.start()
    worker1.join()
    worker2.join()
    worker3.join()