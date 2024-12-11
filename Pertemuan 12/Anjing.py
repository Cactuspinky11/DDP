from Animal import *

class Anjing(Animal):
     def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
         super().__init__(nama, makanan, hidup, berkembang_biak)
         self.jenis = jenis
         self.bunyi = bunyi

     def cetak_anjing(self):
         super().cetak()
         print(f"Jenis \t\t: ", self.jenis, "\nBunyi \t\t: ", self.bunyi)

Pitbull = Anjing("Pitbull", "Daging", "Rumah", "Melahirkan", "corak badak", "haloo sayang")
Pitbull.cetak_anjing()

Bulldog = Anjing("Buldog", "Daging", "Rumah", "Melahirkan", "corak badak", "haloo sayang")
Bulldog.cetak_anjing()
