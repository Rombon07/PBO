# class Segitiga:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def hitung_luas(self):
#         luas = (self.a * self.b) / 2
#         return luas

#     def hitung_keliling(self):
#         keliling = self.a + self.b + self.c
#         return keliling


# def main():
#     print("Program Menghitung Luas dan Keliling Segitiga")
#     while True:
#         print("\nPilih operasi yang ingin Anda lakukan:")
#         print("1. Hitung Luas")
#         print("2. Hitung Keliling")
#         print("3. Keluar")

#         pilihan = input("Masukkan pilihan (1/2/3): ")

#         if pilihan == "1":
#             a = float(input("Masukkan panjang alas: "))
#             b = float(input("Masukkan tinggi: "))
#             segitiga = Segitiga(a, b, 0)
#             luas = segitiga.hitung_luas()
#             print(f"Luas segitiga adalah: {luas} cm^2")

#         elif pilihan == "2":
#             a = float(input("Masukkan panjang sisi a: "))
#             b = float(input("Masukkan panjang sisi b: "))
#             c = float(input("Masukkan panjang sisi c: "))
#             segitiga = Segitiga(a, b, c)
#             keliling = segitiga.hitung_keliling()
#             print("Keliling segitiga adalah:", keliling)

#         elif pilihan == "3":
#             print("Terima kasih!")
#             break

#         else:
#             print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


# if __name__ == "__main__":
#     main()


class DeretanAngka:
    def __init__(self):
        self.nim = ""

    def set_nim(self, nim):
        if len(nim) != 2 or not nim.isdigit():
            print("harus berupa 2 digit angka.")
            return False
        self.nim = nim
        return True

    def tampilkan_deret(self):
        if not self.nim:
            print("Masukkan NIM :")
            return
        print("Deret angka dari 1 sampai 50 (kecuali 2 digit terakhir dari NIM):")
        for i in range(1, 51):
            if str(i)[-2:] != self.nim:
                print(i, end=" ")


deret = DeretanAngka()
nim = input("Masukkan 2 digit terakhir NIM Anda: ")
if deret.set_nim(nim):
    deret.tampilkan_deret()
