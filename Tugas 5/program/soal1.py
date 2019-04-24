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
    global Jkiri 
    Jkiri = random.randrange(1,100)
    kiri.send(Jkiri)
    print('Jarak kiri mobil : ',Jkiri,' cm')
    kiri.close()

def SensorKanan(kanan):
    Jkanan = random.randrange(1,100)
    kanan.send(Jkanan)
    print('Jarak kanan mobil : ',Jkanan,' cm')
    kanan.close()

def SensorTraffic(traffic):
    list = ['merah','kuning','hijau']
    lampu = random.choice(list)
    traffic.send(lampu)
    print('Lampu traffic sedang : ',lampu)
    traffic.close()

def Controller(depan,belakang,kiri,kanan,lampu):
    DP = depan.recv()
    BK = belakang.recv()
    KI = kiri.recv()
    KA = kanan.recv()
    LP = lampu.recv()

    print('--- Tindakan ---')
    command(DP,BK,KI,KA,LP)

if __name__ == '__main__':
    while(1):
        depanIn,depanOut        = Pipe()
        belakangIn,belakangOut  = Pipe()
        kiriIn,kiriOut          = Pipe()
        kananIn,kananOut        = Pipe()
        lampuIn,lampuOut        = Pipe()
        
        KirimSensorDepan        = Process(target=SensorDepan,args=(depanIn,))
        KirimSensorBelakang     = Process(target=SensorBelakang,args=(belakangIn,))
        KirimSensorKiri         = Process(target=SensorKiri,args=(kiriIn,))
        KirimSensorKanan        = Process(target=SensorKanan,args=(kananIn,))
        KirimLampu              = Process(target=SensorTraffic,args=(lampuIn,))
        ControllerUtama         = Process(target=Controller,args=(depanOut,belakangOut,kiriOut,kananOut,lampuOut))

        KirimLampu.start()
        KirimSensorDepan.start()
        KirimSensorBelakang.start()
        KirimSensorKiri.start()
        KirimSensorKanan.start()
        ControllerUtama.start()

        KirimLampu.join()
        KirimSensorDepan.join()
        KirimSensorBelakang.join()
        KirimSensorKiri.join()
        KirimSensorKanan.join()
        ControllerUtama.join()

        time.sleep(1)