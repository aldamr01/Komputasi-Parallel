import random
import time
import multiprocessing

def SoalA():    
    for i in range(0,10):
        if i%2==1:            
            print("==Proses 1=>-----",i)        
        time.sleep(random.randrange(1,2))

def SoalB():    
    for i in range(50,60):
        if i%2==0:            
            print("==Proses 2=>----------",i)
        time.sleep(random.randrange(1,2))
    
def SoalC():    
    for i in range(0,5):                
        print("==Proses 3=>---------------",random.randrange(100,500))
        time.sleep(random.randrange(1,2))
    

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