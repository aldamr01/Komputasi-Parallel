from multiprocessing import Process, Pipe
from random import randint
import time
import random

DataSensor = [[500,400,300,200,100],[500,400,300,200,100],[600,500,400,300,200],[500,400,300,200,100],[40,30,20,10,5],[60,40,30,20,10],[500,400,300,200,100],["Merah","Kuning","Hijau"]]
L = ['Terus','Terus','Belok Kiri', 'Terus', 'Belok Kanan','Terus']
V=60
Gas=0
Vbaru=0

def lintasan(koneksi):
	global k
	global alurLintasan
	k=0
	while k<10:
		k=randint(0,5)
		alurLintasan=L[k]
		koneksi.send(["sensor lintasan",alurLintasan])
		k+=1
		time.sleep(1)

def depanKiri(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jDepanKiri=DataSensor[0][k]
		koneksi.send(["sensor depan kiri",jDepanKiri])
		k+=1
		time.sleep(1)

def depanKanan(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jDepanKanan=DataSensor[1][k]
		koneksi.send(["sensor depan kanan",jDepanKanan])
		k+=1
		time.sleep(1)

def depan(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jarakDepan=DataSensor[2][k]
		koneksi.send(["sensor depan",jarakDepan])
		k+=1
		time.sleep(1)

def belakang(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jarakBelakang=DataSensor[3][k]
		koneksi.send(["sensor belakang",jarakBelakang])
		k+=1
		time.sleep(1)

def sampingKiri(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jarakKiri=DataSensor[4][k]
		koneksi.send(["sensor kiri",jarakKiri])
		k+=1
		time.sleep(1)

def sampingKanan(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jarakKanan=DataSensor[5][k]
		koneksi.send(["sensor kanan",jarakKanan])
		k+=1
		time.sleep(1)

def jLampu(koneksi):
	global k
	k=0
	while k<10:
		k=randint(0,4)
		jarakLampu=DataSensor[6][k]
		koneksi.send(["sensor jarak lampu lalu lintas",jarakLampu])
		k+=1
		time.sleep(1)

def lampuLalin(koneksi):
	k=0
	while k<10:
		k=randint(0,2)
		lampu=DataSensor[7][k]
		koneksi.send(["sensor lampu lalu lintas",lampu])
		k+=1
		time.sleep(1)

def masterControl(koneksi):
	global JTempuh
	global JWaktu
	JTempuh=0
	JWaktu=0
	print("---------- Start ----------\n\n")
	while JTempuh<3000:
		vList=koneksi.recv()
		sensor=vList[0]
		inputan=vList[1]

		print("[",vList[0],"=",vList[1],"]")
		if sensor=="sensor depankiri":
			if inputan>300:
				Gas=0
				Vbaru=(V+Gas)
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil berjalan lurus dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan<=300:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengurangi kecepatan dengan kecepatan saat ini: ",Vbaru,"km/jam dan belok kiri\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		elif sensor=="sensor depankanan":
			if inputan>300:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil berjalan lurus dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan<=300:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengurangi kecepatan dengan kecepatan saat ini: ",Vbaru,"km/jam dan belok kanan\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		elif sensor=="sensor depan":
			if inputan>400:
				Gas=(((inputan-400)/100)*3.6)
				Vbaru=(V+Gas)
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil menambah kecepatan: ",Gas,"km/jam. Kecepatan sekarang: ",Vbaru,"km/jam .Jarak kendaraan di depan: ",inputan,"cm\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan<=400:
				Gas=(((400-inputan)/100)*3.6)
				Vbaru=(V-Gas)
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengurangi kecepatan: ",Gas,"km/jam. Kecepatan sekarang: ",Vbaru,"km/jam. Jarak kendaraan di depan: ",inputan,"cm\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		elif sensor=="sensor belakang":
			if inputan>400:
				print("Mobil berjalan, jarak kendaraan di belakang :",inputan,"cm\n\n")
			elif inputan<=400:
				Gas=(((400-inputan)/100)*3.6)
				Vbaru=(V+Gas)
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengurangi kecepatan: ",Gas,"km/jam. Kecepatan sekarang: ",Vbaru,"km/jam. Jarak kendaraan di depan: ",inputan,"cm\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		elif sensor=="sensor kanan":
			if inputan>=30:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil berjalan, jarak samping kanan kendaraan:",inputan,"cm dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan<30:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Belok kiri kurang lebih sejauh",40-inputan,"cm dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")			
		elif sensor=="sensor kiri":
			if inputan>=20:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil berjalan, jarak samping kiri kendaran",inputan,"cm dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh,"meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan<20:
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Belok kanan kurang lebih sejauh",80-inputan,"cm dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		elif sensor=="sensor lampulalin":
			if inputan=="Hijau":
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil Berjalan dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan=="Kuning":
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengurangi kecepatan, siap-siap untuk berhenti dengan kecepatan saat ini: ",Vbaru,"km/jam\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
			elif inputan=="Merah":
				JTempuh=JTempuh+(Vbaru/1)
				JWaktu+=1
				print("Mobil mengerem, dan berhenti.\nJarak tempuh saat ini: ",JTempuh," meter\nDengan catatan waktu: ",JWaktu," menit\n\n")
		time.sleep(1)
	else:
		print("Anda telah sampai tujuan dengan Jarak Tempuh 30 KM")

if __name__=="__main__":
	PipaIN, PipaOUT = Pipe()
	ProsesLintasan=Process(target=lintasan,args=(PipaIN,))
	ProsesDepanKiri=Process(target=depanKiri,args=(PipaIN,))
	ProsesDepanKanan=Process(target=depanKanan,args=(PipaIN,))
	ProsesDepan=Process(target=depan,args=(PipaIN,))
	ProsesBelakang=Process(target=belakang,args=(PipaIN,))
	ProsesKiri=Process(target=sampingKiri,args=(PipaIN,))
	ProsesKanan=Process(target=sampingKanan,args=(PipaIN,))
	ProsesLalin=Process(target=lampuLalin,args=(PipaIN,))
	ProsesKendali=Process(target=masterControl,args=(PipaOUT,))

	ProsesLintasan.start()
	ProsesDepanKiri.start()
	ProsesDepanKanan.start()
	ProsesDepan.start()
	ProsesBelakang.start()
	ProsesKiri.start()
	ProsesKanan.start()
	ProsesLalin.start()
	ProsesKendali.start()

	ProsesLintasan.join()
	ProsesDepanKiri.join()
	ProsesDepanKanan.join()
	ProsesDepan.join()
	ProsesBelakang.join()
	ProsesKiri.join()
	ProsesKanan.join()
	ProsesLalin.join()
	ProsesKendali.join()