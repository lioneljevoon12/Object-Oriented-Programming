class Novel:
    def __init__(self, judul, nama_pengarang, tahun_terbit,
                 deskripsi, harga_beli):
        self.judul = judul
        self.nama_pengarang = nama_pengarang
        self.tahun_terbit = tahun_terbit
        self.deskripsi = deskripsi
        self.__harga_beli = harga_beli  # atribut private
 
    # Getter -> untuk membaca harga beli
    def get_harga_beli(self):
        return self.__harga_beli
 
    # Setter -> untuk mengubah harga beli dengan validasi
    def set_harga_beli(self, harga_baru):
        if harga_baru > 0:
            self.__harga_beli = harga_baru
        else:
            print("Harga beli harus lebih besar dari 0!!!")
 
    # Hitung harga jual (harga beli - 20% dari harga beli)
    def harga_jual(self):
        return self.__harga_beli - (0.20 * self.__harga_beli)
 
    # Tampilkan informasi novel
    def info_novel(self):
        print(f"Judul          : {self.judul}")
        print(f"Nama Pengarang : {self.nama_pengarang}")
        print(f"Tahun Terbit   : {self.tahun_terbit}")
        print(f"Deskripsi      : {self.deskripsi}")
        print(f"Harga Beli     : Rp {self.get_harga_beli():,.0f}")
        print(f"Harga Jual     : Rp {self.harga_jual():,.0f}")
        print("-" * 40)

# Membuat 3 objek novel
novel1 = Novel("A Study in Scarlet", "Arthur Conan Doyle", 1887,
               "Awal kisah Sherlock Holmes dan Dr. Watson.",
               80000)
novel2 = Novel("Murder on the Orient Express", "Agatha Christie", 1934,
               "Poirot mengusut pembunuhan di kereta terjebak salju.",
               120000)
novel3 = Novel("The Hound of the Baskervilles", "Arthur Conan Doyle", 1902,
               "Holmes menyelidiki legenda anjing hantu Baskerville.",
               100000)

# Tampilkan informasi setiap novel
novel1.info_novel()
novel2.info_novel()
novel3.info_novel()
 
# Hitung total harga beli & total harga jual
total_beli = (novel1.get_harga_beli()
              + novel2.get_harga_beli()
              + novel3.get_harga_beli())
total_jual = (novel1.harga_jual()
              + novel2.harga_jual()
              + novel3.harga_jual())
 
print(f"Total Harga Beli : Rp {total_beli:,.0f}")
print(f"Total Harga Jual : Rp {total_jual:,.0f}")