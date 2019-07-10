# EVALUASI AKHR SEMESTER GENAP 2019
# Membuat simulasi Program Kontrol Ruangan Informatika mulai Q301 sd Q307
# Agar nyaman dan efisien penggunakan daya listrik, keawetan sarana
# Menampilkan ruang Q301 sd Q307 dengan status & Keterangan sebagi contoh berikut;
# Q301: AC Nyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Kuliah
# Q302: AC Nyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong
# Q303: AC Mati, Lampu Mati, LCD Mati, Kosong, Kuliah Kosong
# dll

# EAS Komputasi Paralel Klas:S =======================
# NBI: 1461600045           Nama: Bagus Setyo Budi
#-----------------------------------------------------
import time
from threading import Thread
from random import randint
from queue import Queue

# Mengukur Suhu Ruangan yang ber-AC 
# simulasi int antara 18 sd 40, untuk ruang kelas dijaga 25-28 derajat Celcius 
def BacaSuhuRuang(output_queu):
    while True:
        data = {
            0 : "suhuRuang",
            1 : [
                ['Q301', randint(18, 40)],
                ['Q302', randint(18, 40)],
                ['Q303', randint(18, 40)],
                ['Q304', randint(18, 40)],
                ['Q305', randint(18, 40)],
                ['Q306', randint(18, 40)],
                ['Q307', randint(18, 40)],
            ]
        }
        output_queu.put(data)
        time.sleep(1)

# Mengukur keberadaan manusia dengan Sensor Suhu Tubuh manusia  
# simulasi int antara 18 sd 40, untuk manusia normal suhunya 33,2-38,2°C 
def BacaSuhuTubuh(output_queu):
    while True:
        data = {
            0 : "suhuTubuh",
            1 : [
                ['Q301', randint(18, 40)],
                ['Q302', randint(18, 40)],
                ['Q303', randint(18, 40)],
                ['Q304', randint(18, 40)],
                ['Q305', randint(18, 40)],
                ['Q306', randint(18, 40)],
                ['Q307', randint(18, 40)],
            ]
        }
        output_queu.put(data)
        time.sleep(1)

# Mengukur cahaya (Luminasi dg satuan Lux)
# simulasi int antara 1 sd 10000, untuk kantor/ruang kelas dijaga 320 - 500 lux
def BacaLuminasiRuang(output_queu):
    while True:
        data = {
            0 : "luminasiRuang",
            1 : [
                ['Q301', randint(1, 10000)],
                ['Q302', randint(1, 10000)],
                ['Q303', randint(1, 10000)],
                ['Q304', randint(1, 10000)],
                ['Q305', randint(1, 10000)],
                ['Q306', randint(1, 10000)],
                ['Q307', randint(1, 10000)],
            ]
        }
        output_queu.put(data)
        time.sleep(1)

def BacaJamRuang(output_queu):
    while True:
        data = {
            0 : "jamRuang",
            1 : [
                ['Q301', randint(1, 24)],
                ['Q302', randint(1, 24)],
                ['Q303', randint(1, 24)],
                ['Q304', randint(1, 24)],
                ['Q305', randint(1, 24)],
                ['Q306', randint(1, 24)],
                ['Q307', randint(1, 24)],
            ]
        }
        output_queu.put(data)
        time.sleep(1)

#Aturan dan Data Aktifitas Kantor adalah sbb;
# Sumulasi jam akan berjalan dari 1 sd 24.
# Q307 beroperasi sesuai jam kantor Senin sd Jumat pk.7.00 sd 21.00
# Setiap ada jadwal kuliah LCD pasti menyala, dan dimatikan selesai kuliah
# Lampu kelas dan AC akan dimatikan jika tidak ada mahasiswa didalamnya
# Q301 sd Q306 digunakan sesuai Jadwal kuliah dengan efisien dg simulasi sbb
# Jadwal=[[‘Q307’,7,21],  ['Q302',7,9,1,1],  ['Q305',8,11,1,0],  ['Q306',10,12,1,0], [‘Q303’, 11.13 ,1,1]]
# Contoh Q305: ada jadwal kuliah pk 8 sd 11, 1:ada mhs, Kuliah kosong


# Mahasiswa Informatika sangat antusias dan penuh semangat sehingga setiap ada ruang selalu 
# digunakan untuk kegiatan akademis seperti keminitas Pytho, DSI, Robot, C++, dll sehingga mereka #memiliki jadwal sendiri-sendiri yang terintegrasi. 
# Dalam hal ini disimulasikan sbb;
# JadwalMhs=[ [‘Q305’,11,13, 1], [‘Q304’, 10.13, 0] ]
# Contoh: diruang Q304 mulai pk 10 sd 13 rencana ada kegiatan mhs akan tetapi tidak ada mhsnya


jam = 1
data = [None, None, None, None]

def MasterControl(input_queu):
    while True:
        dt = input_queu.get()
        sensor = dt[0]
        value = dt[1]
        if sensor=="suhuRuang":
            setData(0, value)
        elif sensor=="suhuTubuh":
            setData(1, value)
        elif sensor=="luminasiRuang":
            setData(2, value)
        elif sensor=="jamRuang":
            setData(3, value)
        global data, jam
        if None in data:
            continue
        
        print(" ")
        print("##      Jam ", jam, "      ##", sep="")
        print(" ")
        for i in range(len(data[0])):
            suhuRuang = data[0][i]
            suhuTubuh = data[1][i]
            luminasiRuang = data[2][i]
            jamRuang = data[3][i]
            ruang = "Q30"+str(i+1)
            # adaKuliah = False
            # for j in range(len(jadwal)):
            if ruang == "Q302" and jamRuang == 7 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q302" and jamRuang == 8 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q302" and jamRuang == 9 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q303" and jamRuang == 11 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q303" and jamRuang == 12 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q303" and jamRuang == 13 :
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 8 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 9 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 10 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 11 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 12 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q305" and jamRuang == 13 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Kosong.")
            elif ruang == "Q306" and jamRuang == 10 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q306" and jamRuang == 11 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q306" and jamRuang == 12 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Nyala, Ada Orang, Ada Mahasiswa, Ada Kuliah.")
            elif ruang == "Q307" : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q307 : ", " AC Mati, Lampu Nyala, Ada Orang, Masih Dalam Jam Kerja.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q307 : ", " AC Mati, Lampu Mati, Ada Orang, Masih Dalam Jam Kerja.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q307 : ", " AC Mati, Lampu Nyala, Kosong, Masih Dalam Jam Kerja.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q307 : ", " AC Menyala, Lampu Nyala, Ada Orang, Masih Dalam Jam Kerja.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q307 : ", " AC Menyala, Lampu Mati, Ada Orang, Masih Dalam Jam Kerja.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q307 : ", " AC Menyala, Lampu Nyala, Kosong, Masih Dalam Jam Kerja.")
            elif ruang == "Q301" : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q301 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q301 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q301 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q301 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q301 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q301 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q302" and jamRuang is not 7 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q302" and jamRuang is not 8 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q302" and jamRuang is not 9 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q302 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q302 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q303" and jamRuang is not 11 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q303" and jamRuang is not 13 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q303" and jamRuang is not 14 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q304" : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q304 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q304 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q304 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q304 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q304 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q304 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 8 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 9 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 10 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 11 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 12 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q305" and jamRuang is not 13 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q305 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q305 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q306" and jamRuang is not 10 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q306" and jamRuang is not 11 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q306" and jamRuang is not 12 : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Mati, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Mati, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q306 : ", " AC Menyala, Lampu Mati, LCD Mati, Ada Orang, Kuliah Kosong.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q306 : ", " AC Menyala, Lampu Nyala, LCD Nyala, Kosong, Kuliah Kosong.")
            elif ruang == "Q307" : 
                if suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, Ada Orang, Diluar Jam Kantor.")
                elif suhuRuang >= 28 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Mati, Lampu Mati, Ada Orang, Diluar Jam Kantor.")
                elif suhuRuang >= 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Mati, Lampu Nyala, Kosong, Diluar Jam Kantor.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, Ada Orang, Diluar Jam Kantor.")
                elif suhuRuang < 25 and suhuTubuh >= 38.2 and luminasiRuang < 320 :
                    print ("Q303 : ", " AC Menyala, Lampu Mati, Ada Orang, Diluar Jam Kantor.")
                elif suhuRuang < 28 and suhuTubuh < 33.2 and luminasiRuang >= 500 :
                    print ("Q303 : ", " AC Menyala, Lampu Nyala, Kosong, Diluar Jam Kantor.")

        data = [None, None, None, None]
        jam = jam%24+1
        

def setData(param, value):
    global data
    dt = []
    for i in range(len(value)):
        dt.append(value[i][1])
    data[param] = dt

if __name__ == "__main__":
    
    q = Queue()

    t1 = Thread(target=BacaSuhuRuang, args=(q,))
    t2 = Thread(target=BacaSuhuTubuh, args=(q,))
    t3 = Thread(target=BacaLuminasiRuang, args=(q,))
    t4 = Thread(target=BacaJamRuang, args=(q,))
    t5 = Thread(target=MasterControl, args=(q,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
