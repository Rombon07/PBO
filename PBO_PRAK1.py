# x = int(input("masukan angka pertama :"))
# y = int(input("masukan angka kedua :"))

# z = x + y
# print(f"hasil penjumlahan adalah : {z} ")


# class tambah:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def tambahkan(self):
#         hasil = self.x + self.y
#         return hasil


# penjumlahan = tambah(float(input("masukan nilai1 :")), float(input("masukan nilai2 :")))

# hasil_penjumlahan = penjumlahan.tambahkan()

# print("Hasil penjumlahan:", hasil_penjumlahan)

# self.grades = {
#     "A": (80, 100),
#     "A-": (77, 79.99),
#     "B+": (74, 76.99),
#     "B": (68, 73.99),
#     "B-": (65, 67.99),
#     "C+": (62, 64.99),
#     "C": (56, 61.99),
#     "D": (45, 55.99),
#     "E": (0, 44.99),
# }

# if ipk == 4.00:
#     return "A"
# elif ipk == 3.75:
#     return "A-"
# elif ipk == 3.50:
#     return "B+"
# elif ipk == 3.00:
#     return "B"
# elif ipk == 2.75:
#     return "B-"
# elif ipk == 2.50:
#     return "C+"
# elif ipk == 2.00:
#     return "C"
# elif ipk == 1.00:
#     return "D"
# else:
#     return "E"


class GradeCalculator:
    def __init__(self):
        self.grades = {
            4.00: (80, 100),
            3.75: (77, 79.99),
            3.50: (74, 76.99),
            3.00: (68, 73.99),
            2.75: (65, 67.99),
            2.50: (62, 64.99),
            2.00: (56, 61.99),
            1.00: (45, 55.99),
            0.00: (0, 44.99),
        }

    def calculate_grade(self, score):
        for grade, (lower, upper) in self.grades.items():
            if lower <= score <= upper:
                return grade, self.letter_grade(grade)
        return "Invalid Score"

    def letter_grade(self, grade):
        if grade == 4.00:
            return "A"
        elif grade == 3.75:
            return "A-"
        elif grade == 3.50:
            return "B+"
        elif grade == 3.25:
            return "B"
        elif grade == 3.00:
            return "B-"
        elif grade == 2.75:
            return "C+"
        elif grade == 2.50:
            return "C"
        elif grade == 2.25:
            return "C-"
        elif grade == 2.00:
            return "D"
        else:
            return "E"


def main():
    calculator = GradeCalculator()

    # Input nilai mahasiswa
    nama = input("Nama : ")
    nim = input("Nim : ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    grade_numeric, grade_letter = calculator.calculate_grade(nilai)
    print("--- DATA PRAKTIKUM PBO 2024 ---")
    print(nama)
    print(nim)
    print("")
    print("Grade angka yang didapat:", grade_numeric)
    print("Grade huruf yang didapat:", grade_letter)


if __name__ == "__main__":
    main()
