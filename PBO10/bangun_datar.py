from abc import ABC, abstractmethod
import math


class BangunDatar(ABC):
    @abstractmethod
    def hitungLuas(self):
        pass


class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi**2


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):
        return self.panjang * self.lebar


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitungLuas(self):
        return 0.5 * self.alas * self.tinggi


class Lingkaran(BangunDatar):
    def __init__(self, r):
        self.r = r

    def hitungLuas(self):
        return math.pi * self.r**2


class Layang_layang(BangunDatar):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def hitungLuas(self):
        return 0.5 * self.d1 * self.d2
