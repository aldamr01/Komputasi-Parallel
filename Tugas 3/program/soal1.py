import random
import time
import multiprocessing

def SoalA():    
    for i in range(10,20):
        if i%2 == 1:
            print("==Proses 1=>-----",i)        
        time.sleep(random.randrange(1,2))

def SoalB():    
    for i in range(2,12):
        for o in range(2,i):
            if i%o == 0:
                break
        else:
            print("==Proses 2=>--------",i)    
        time.sleep(random.randrange(1,2))
    
def SoalC():    
    for i in range(50,60):
        if i%2==1:            
            print("==Proses 3=>-----------",i)
        time.sleep(random.randrange(1,2))
    
def SoalD():    
    for i in range(0,5):                
        print("==Proses 4=>--------------",random.randrange(100,200))
        time.sleep(random.randrange(1,2))

if __name__ == "__main__":
    worker1 = multiprocessing.Process(target=SoalA)
    worker2 = multiprocessing.Process(target=SoalB)
    worker3 = multiprocessing.Process(target=SoalC)
    worker4 = multiprocessing.Process(target=SoalD)

    worker1.start()
    worker2.start()
    worker3.start()
    worker4.start()

    worker1.join()
    worker2.join()
    worker3.join()
    worker4.join()