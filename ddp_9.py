print("---- mencari celcius sudut ke fahreinheit ----")
def celcius_ke_fahreinheit(celcius):
    fareinheit = (celcius * 9/5) + 32
    return fareinheit 

print(celcius_ke_fahreinheit(0))
print(celcius_ke_fahreinheit(100))

print("\n---- mencari bilangan genap ----")
def is_genap(bil_genap):
    return bil_genap %2 == 0
# untuk memasukan value
print(is_genap(4))
print(is_genap(7))
print("\n---- mencari rata rata niali ----")
# rata" nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return "Lulus"
    else : 
        return "Gagal"
    
# untuk mencetak value
print(nilai_kelulusan(80)) 
print(nilai_kelulusan(60))  

print("\n---- cetak bilangan ganjil ----")
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
# untuk mencetak value
bil_ganjil(20)

