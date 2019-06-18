from multiprocessing import Process,Pipe

A = 10
B = 10

def kirim(koneksi):
    A = [15,25,35]
    koneksi.send(A)
    print('Nilai yang dikirim :',A,B)
    koneksi.close()

def terima(koneksi):
    print('Nilai yang diterima :',koneksi.recv(),B)

if __name__ == '__main__':
    PipaIn,PipaOut = Pipe()
    ProsesKirim = Process(target=kirim,args=(PipaIn,))
    ProsesTerima = Process(target=terima,args=(PipaOut,))

    ProsesKirim.start()
    ProsesTerima.start()

    ProsesKirim.join()
    ProsesTerima.join()