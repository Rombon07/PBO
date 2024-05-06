# import math


# class BangunRuang:
#     @staticmethod
#     def volume(
#         sisi=None, panjang=None, lebar=None, tinggi=None, jari_jari=None, args=None
#     ):
#         if args == 1:
#             return sisi**3
#         elif args == 2:
#             return (4 / 3) * math.pi * (jari_jari**3)
#         elif args == 3:
#             return panjang * lebar * tinggi


# volume_kubus = BangunRuang.volume(sisi=2, args=1)
# volume_bola = BangunRuang.volume(jari_jari=7, args=2)
# volume_balok = BangunRuang.volume(panjang=3, lebar=1, tinggi=2, args=3)

# print("\nNama : Yustianas Rombon \nNim : 064002300015\n")

# print("Volume Kubus:", volume_kubus)
# print("Volume Balok:", volume_balok)
# print("Volume Bola:", volume_bola)


class p9e2:
    @staticmethod
    def methodTambah(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return p9e2.methodTambahInt(x, y)
        elif isinstance(x, float) or isinstance(y, float):
            return p9e2.methodTambahFloat(x, y)
        else:
            raise TypeError("Tipe data tidak didukung")

    @staticmethod
    def methodTambahInt(x, y):
        return x + y

    @staticmethod
    def methodTambahFloat(x, y):
        return x + y


myNum1 = p9e2.methodTambah(8, 5)
myNum2 = p9e2.methodTambah(4.5, 6.5)
print("int :", myNum1)
print("float :", myNum2)
