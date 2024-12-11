from Animal import *

class Burung(Animal):
     def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
         super().__init__(nama, makanan, hidup, berkembang_biak)
         self.jenis = jenis
         self.bunyi = bunyi

     def cetak_burung(self):
         super().cetak()
         print(f"Jenis \t\t: ", self.jenis, "\nBunyi \t\t: ", self.bunyi)

Kakatua = Burung("Kaka tua", "Temen", "Pohon", "Bertelur", "corak badak", "Monyeeetttt")
Kakatua.cetak_burung()

Beo = Burung("Beo", "Biji Bijian", "Pohon", "Bertelur", "corak badak", "Monyeeetttt")
Beo.cetak_burung()