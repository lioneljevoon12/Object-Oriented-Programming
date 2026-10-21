class Laptop:
    def __init__(self, merek, model, tahun, spesifikasi, harga_beli):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.spesifikasi = spesifikasi
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

    # Hitung harga jual (harga beli + 25% dari harga beli)
    def hitung_harga_jual(self):
        return self.__harga_beli + (0.25 * self.__harga_beli)

    # Tampilkan informasi laptop
    def tampil_info(self):
        print(f"Laptop: {self.merek} {self.model}")
        print(f"Tahun: {self.tahun}")
        print(f"Spesifikasi: {self.spesifikasi}")
        print(f"Harga Beli: Rp {self.get_harga_beli():,.0f}")
        print(f"Harga Jual: Rp {self.hitung_harga_jual():,.0f}")
        print("-" * 40)


# Membuat beberapa objek laptop
laptop1 = Laptop("Asus", "VivoBook 14", 2022,
                 "i5, 8GB RAM, 512GB SSD", 8000000)
laptop2 = Laptop("Lenovo", "ThinkPad X1", 2021,
                 "i7, 16GB RAM, 1TB SSD", 15000000)
laptop3 = Laptop("HP", "Pavilion 15", 2020,
                 "Ryzen 5, 8GB RAM, 512GB SSD", 10000000)

# Tampilkan informasi setiap laptop
laptop1.tampil_info()
laptop2.tampil_info()
laptop3.tampil_info()

# Hitung total harga beli & jual semua laptop
total_beli = (laptop1.get_harga_beli()
              + laptop2.get_harga_beli()
              + laptop3.get_harga_beli())
total_jual = (laptop1.hitung_harga_jual()
              + laptop2.hitung_harga_jual()
              + laptop3.hitung_harga_jual())

print(f"Total Harga Beli: Rp {total_beli:,.0f}")
print(f"Total Harga Jual: Rp {total_jual:,.0f}")

print("\n== Ubah harga beli laptop1 ==")
laptop1.set_harga_beli(8500000)   # ubah harga beli
laptop1.tampil_info()

# coba setter dengan nilai salah
laptop1.set_harga_beli(-5000000)  # seharusnya muncul pesan error