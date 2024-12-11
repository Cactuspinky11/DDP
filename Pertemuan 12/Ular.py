from Animal import *

class Ular(Animal):
     def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
         super().__init__(nama, makanan, hidup, berkembang_biak)
         self.design = design
         self.racun = racun

     def cetak_ular(self):
         super().cetak()
         print(f"Design \t\t: ", self.design, "\nRacun \t\t: ", self.racun)

anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

Boa = Ular("Boa", "Kambing", "Sungai", "Bertelur", "Batik Solo", "Tidak Berbisa")
Boa.cetak_ular()
    

