print("Kalkulator Sederhana")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
print("-------------------------------------")


#Logic

def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

tipe = input("silahkan masukkan nomor yang anda pilih: ?\n")

if tipe in ("1","2","3","4",):
    angka1 = int(input("angka pertama:\n"))
    angka2 = int(input("angka kedua:\n"))
    print("-----------------------------")
    
    if tipe == "1":
        print("Jawabannya adalah :", penjumlahan(angka1, angka2))
    if tipe == "2":
        print("Jawabannya adalah :", pengurangan(angka1, angka2))
    if tipe == "3":
        print("Jawabannya adalah :", perkalian(angka1, angka2))
    if tipe == "4":
        print("Jawabannya adalah :", pembagian(angka1, angka2))
    
    