import math

class BangunRuang:
    def __init__(self, nama):
        self.nama = nama

    def luas(self):
        pass

    def volume(self):
        pass


class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__("Kubus")
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi**2

    def volume(self):
        return self.sisi**3


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * (
            self.panjang * self.lebar
            + self.panjang * self.tinggi
            + self.lebar * self.tinggi
        )

    def volume(self):
        return self.panjang * self.lebar * self.tinggi


class PrismaSegiTiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi):
        super().__init__("Prisma Segitiga")
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi = tinggi

    def luas(self):
        return (self.alas * self.tinggi_alas) + (3 * self.alas * self.tinggi)

    def volume(self):
        return 0.5 * self.alas * self.tinggi_alas * self.tinggi


class LimasSegiEmpat(BangunRuang):
    def __init__(self, panjang_alas, lebar_alas, tinggi):
        super().__init__("Limas Segi Empat")
        self.panjang_alas = panjang_alas
        self.lebar_alas = lebar_alas
        self.tinggi = tinggi

    def luas(self):
        return (
            (2 * self.panjang_alas * self.lebar_alas)
            + (
                self.panjang_alas
                * math.sqrt((self.lebar_alas / 2) ** 2 + self.tinggi**2)
            )
            + (
                self.lebar_alas
                * math.sqrt((self.panjang_alas / 2) ** 2 + self.tinggi**2)
            )
        )

    def volume(self):
        return (self.panjang_alas * self.lebar_alas * self.tinggi) / 3


class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__("Bola")
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari**2

    def volume(self):
        return (4 / 3) * math.pi * self.jari_jari**3


print("Nama : Yustianas Rombon")
print("Nim  : 064002300015")

kubus = Kubus(5)
print(f"\nLuas Kubus: {kubus.luas()}")
print(f"Volume Kubus: {kubus.volume()}")

balok = Balok(4, 6, 8)
print(f"\nLuas Balok: {balok.luas()}")
print(f"Volume Balok: {balok.volume()}")

prisma = PrismaSegiTiga(6, 8, 10)
print(f"\nLuas Prisma Segitiga: {prisma.luas()}")
print(f"Volume Prisma Segitiga: {prisma.volume()}")

limas = LimasSegiEmpat(6, 8, 10)
print(f"\nLuas Limas Segi Empat: {limas.luas()}")
print(f"Volume Limas Segi Empat: {limas.volume()}")

bola = Bola(7)
print(f"\nLuas Bola: {bola.luas()}")
print(f"Volume Bola: {bola.volume()}")
