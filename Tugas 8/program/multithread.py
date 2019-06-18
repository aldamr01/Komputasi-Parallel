from queue import Queue
from threading import Thread
import random
import time

def Depan(output_depan):
    Depan=0
    while Depan<60:
        data = {1:random.randrange(10,100)}
        output_depan.put(data)
        Depan+=1

def InputDepan(input_depan):
    i=0
    while i<10:
        data = input_depan.get()
        print("Sensor depan : " ,data[1])
        input_depan.task_done()
        i+=1
        time.sleep(3)

def Belakang(output_belakang):
    Belakang=0
    while Belakang<60:
        data = {1:random.randrange(10,100)}
        output_belakang.put(data)
        Belakang+=1

def InputBelakang(input_belakang):
    k=0
    while k<10:
        data = input_belakang.get()
        print("Sensor belakang : " ,data[1])
        input_belakang.task_done()
        k+=1
        time.sleep(3)

def Kanan(output_kanan):
    Kanan=0
    while Kanan<60:
        data = {1:random.randrange(10,100)}
        output_kanan.put(data)
        Kanan+=1

def InputKanan(input_kanan):
    k=0
    while k<10:
        data = input_kanan.get()
        print("Sensor kanan : " ,data[1])
        input_kanan.task_done()
        k+=1
        time.sleep(3)

def Kiri(output_kiri):
    Kiri=0
    while Kiri<60:
        data = {1:random.randrange(10,100)}
        output_kiri.put(data)
        Kiri+=1

def InputKiri(input_kiri):
    k=0
    while k<10:
        data = input_kiri.get()
        print("Sensor kiri : " ,data[1])
        input_kiri.task_done()
        k+=1
        time.sleep(3)


#shred Queue
q=Queue()
t1=Thread(target=InputDepan, args=(q,))
t2=Thread(target=Depan, args=(q,))
t3=Thread(target=InputBelakang, args=(q,))
t4=Thread(target=Belakang, args=(q,))
t5=Thread(target=InputKanan, args=(q,))
t6=Thread(target=Kanan, args=(q,))
t7=Thread(target=InputKiri, args=(q,))
t8=Thread(target=Kiri, args=(q,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()