''' Membuat Hitungan Persegi Panjang'''

import os

def header():
    os.system('cls')
    print(f"{'Program perhitungan Luas':^40}")
    print(f"{'dan Keliling Persegi Panjang:':^40}")
    print(f"{'='*40:^40}")

def input_user():
    panjang = int(input("Masukan Nilai Panjang = "))
    lebar = int(input("Masukan Nilai Lebar = "))

    return panjang, lebar

def luas(panjang, lebar):
    return panjang * lebar

def Keliling(panjang, lebar):
    return 2 * (panjang + lebar)

def display(message, value):
    print(f"Hasil dari perhitungan {message} = {value}")

while True:
    header()
    PANJANG, LEBAR = input_user()
    HITUNGAN_LUAS = luas(PANJANG, LEBAR)
    HITUNGAN_KELILING = Keliling(PANJANG, LEBAR)
    display("Luas", HITUNGAN_LUAS)
    display("Keliling", HITUNGAN_KELILING)
    
    incontinue = input("Apakah anda ingin lanjut atau tidak? (y/n)").lower()
    if incontinue == 'n':
        break

print("Program Telah Selesai")