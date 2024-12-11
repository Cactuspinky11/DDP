class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("\n Nama \t\t: ", self.nama,
              "\n makanan \t: ", self.makanan,
              "\n hidup \t\t: ", self.hidup,
              "\n berkembnag_biak: ", self.berkembang_biak,
              )

