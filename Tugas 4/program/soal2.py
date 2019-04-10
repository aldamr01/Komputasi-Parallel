from fuzzy import command
from multiprocessing import Process,Pipe
import random
import time

def SensorDepan(depan):
    Jdepan = random.randrange(1,100)
    depan.send(Jdepan)
    print('Jarak depan mobil : ',Jdepan,' cm')
    depan.close()

def SensorBelakang(belakang):
    Jbelakang = random.randrange(1,100)
    belakang.send(Jbelakang)
    print('Jarak belakang mobil : ',Jbelakang,' cm')
    belakang.close()

def SensorKiri(kiri):
    Jkiri = random.randrange(1,100)
    kiri.send(Jkiri)
    print('Jarak kiri mobil : ',Jkiri,' cm')
    kiri.close()

def SensorKanan(kanan):
    Jkanan = random.randrange(1,100)
    kanan.send(Jkanan)
    print('Jarak kanan mobil : ',Jkanan,' cm')
    kanan.close()

def TerimaSensor(depan,belakang,kiri,kanan):
    DP = depan.recv()
    BK = belakang.recv()
    KI = kiri.recv()
    KA = kanan.recv()
    
    print('--- Tindakan ---')
    command(DP,BK,KI,KA)

if __name__ == '__main__':
    depanIn,depanOut = Pipe()
    belakangIn,belakangOut = Pipe()
    kiriIn,kiriOut = Pipe()
    kananIn,kananOut = Pipe()
    
    KirimSensorDepan = Process(target=SensorDepan,args=(depanIn,))
    KirimSensorBelakang = Process(target=SensorBelakang,args=(belakangIn,))
    KirimSensorKiri = Process(target=SensorKiri,args=(kiriIn,))
    KirimSensorKanan = Process(target=SensorKanan,args=(kananIn,))
    TerimaSensorSemua = Process(target=TerimaSensor,args=(depanOut,belakangOut,kiriOut,kananOut))

    KirimSensorDepan.start()
    KirimSensorBelakang.start()
    KirimSensorKiri.start()
    KirimSensorKanan.start()
    TerimaSensorSemua.start()

    KirimSensorDepan.join()
    KirimSensorBelakang.join()
    KirimSensorKiri.join()
    KirimSensorKanan.join()
    TerimaSensorSemua.join()