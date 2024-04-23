# class Film:
#     def __init__(self):
#         self.daftar_film = []

#     def tambah_film(self, judul):
#         self.daftar_film.append(judul)

#     def tampilkan_film(self):
#         print("5 film favorit kamu nich:")
#         for film in self.daftar_film:
#             print(film)


# def main():
#     film_favorit = Film()

#     print("-----Elkom 1-----")
#     for i in range(5):
#         film_favorit.tambah_film(input(f"Film favorite ke-{i+1}: "))

#     print("\n===Daftar Film Favorite===")
#     film_favorit.tampilkan_film()


# if __name__ == "__main__":
#     main()


class Film:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, judul, tahun_rilis, direktor):
        self.daftar_film.append(
            {"Judul": judul, "Tahun Rilis": tahun_rilis, "Director": direktor}
        )

    def tampilkan_film(self):
        print("\n===Daftar Film Favorit===")
        for i, film in enumerate(self.daftar_film, 1):
            print(f"judul film favorit ke - {i}:")
            print(f"judul : {film['Judul']}")
            print(f"rilis : {film['Tahun Rilis']}")
            print(f"director : {film['Director']}")
            print()

def main():
    film_favorit = Film()
    print("----- elkom 2 -----")
    # Menambahkan film-film favorit secara langsung
    film_favorit.tambah_film("Laskar Pelangi", "2008", "Riri Riza")
    film_favorit.tambah_film("Ada Apa dengan Cinta?", "2002", "Rudi Soedjarwo")
    film_favorit.tambah_film("Inception", "2010", "Christopher Nolan")
    film_favorit.tambah_film("The Godfather", "1972", "Francis Ford Coppola")
    film_favorit.tambah_film("Interstellar", "2014", "Christopher Nolan")

    # Menampilkan daftar film favorit
    film_favorit.tampilkan_film()


if __name__ == "__main__":
    main()
