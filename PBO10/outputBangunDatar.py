from bangun_datar import Persegi, PersegiPanjang, Segitiga, Lingkaran, Layang_layang  # type: ignore


print("Nama: Yustianas Rombon\nNim: 064002300015\n")

persegi = Persegi(4)
print("Luas Persegi:", persegi.hitungLuas())

persegi_panjang = PersegiPanjang(4, 6)
print("Luas Persegi Panjang:", persegi_panjang.hitungLuas())

segitiga = Segitiga(5, 7)
print("Luas Segitiga:", segitiga.hitungLuas())

lingkaran = Lingkaran(14)
print("Luas Lingkaran:", lingkaran.hitungLuas())

layang_layang = Layang_layang(7, 9)
print("Luas Layang-layang:", layang_layang.hitungLuas())
