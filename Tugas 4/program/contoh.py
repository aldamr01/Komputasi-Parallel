A = 10

def kirim():
    B = 15
    global C
    C = 25
    print("1. Modul kirim : Nilai A,B,B :",A,B,C)

def terima():
    print("2. Modul terima : Nilai A,B,C :",A,B,C)

B = 10

kirim()
terima()