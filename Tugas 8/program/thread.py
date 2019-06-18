from queue import Queue
from threading import Thread
import random


def Producer(output_queu):
    k=0
    while k<10:
        data ={1: random.randrange(50,200)}
        output_queu.put(data)
        k+=1
def Consumer(input_queue):
    i=0
    while i<10:
        data=input_queue.get()
        print(data[1])
        input_queue.task_done()
        i+=1
#shred Queue
q=Queue()
t1=Thread(target=Consumer, args=(q,))
t2=Thread(target=Producer, args=(q,))
t1.start()
t2.start()