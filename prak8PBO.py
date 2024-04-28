class MasyarakatKampus:
    def __init__(self, gaji=150000, golongan="LAINNYA"):
        self.__gaji = gaji
        self.__golongan = golongan

    def gaji(self):
        return self.__gaji

    def penjelasan(self):
        print("Golongan", self.__golongan, "mendapatkan gaji =", self.__gaji)


class Dosen(MasyarakatKampus):
    def __init__(self, gaji=150000):
        super().__init__(gaji + 300000, "DOSEN")


class Staff(MasyarakatKampus):
    def __init__(self, gaji=150000):
        super().__init__(gaji + 150000, "STAFF")


print("Nama : Yustianas Rombon\nNim :064002300015\n")
dosen = Dosen()
staff = Staff()
lainnya = MasyarakatKampus()

dosen.penjelasan()
staff.penjelasan()
lainnya.penjelasan()
