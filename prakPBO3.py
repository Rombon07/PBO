class saya:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def show(self):
        print("Nama saya adalah ", self.nama, "nim saya ", self.nim)
        print("saya dari fakultas ", self.fakultas)
        print("Hobi saya adalah ", self.hobi)


biodata = saya("Yustianas Rombon", "064002300015", "Teknik Informatika", "nyari takjil")

biodata.show()


# class persegi_panjang:
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar = lebar

#     def hitung_luas(self):
#         luas = self.panjang * self.lebar
#         return luas

#     def show(self):
#         print(
#             "persegi panjang dengan panjang ",
#             self.panjang,
#             "dan lebar ",
#             self.lebar,
#             "memiliki luas sebesar ",
#             self.hitung_luas(),
#             "cm^2",
#         )


# if __name__ == "__main__":
#     output = persegi_panjang(20, 12)
#     output.show()
