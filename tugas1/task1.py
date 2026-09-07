class Mahasiswa:
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    #object pertama

mahasiswa1 = Mahasiswa("Nando Abdillah Salam", "2025A", "123456789", "Teknik Informatika", "Fakultas Teknik", "Universitas Negeri Surabaya")
print("Data Mahasiswa 1", "\nNama:", mahasiswa1.nama, "\nKelas:", mahasiswa1.kelas, 
        "\nNIM:", mahasiswa1.nim, "\nJurusan:", mahasiswa1.jurusan, "\nFakultas:", mahasiswa1.fakultas, "\nKampus:", mahasiswa1.kampus)

mahasiswa2 = Mahasiswa("Lionel Jevon", "2025A", "987654321", "Manajemen Informatika", "Fakultas Vokasi", "Universitas Negeri Surabaya")
print("Data Mahasiswa 2", "\nNama:", mahasiswa2.nama, "\nKelas:", mahasiswa2.kelas, 
        "\nNIM:", mahasiswa2.nim, "\nJurusan:", mahasiswa2.jurusan, "\nFakultas:", mahasiswa2.fakultas, "\nKampus:", mahasiswa2.kampus)