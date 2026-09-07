class Mobil:
    # Ini adalah Method
    def klakson(self):
        print("Din din!")

mobil_pertama = Mobil()

# Menambahkan Atribut secara manual dari luar
mobil_pertama.warna = "Merah"
print(mobil_pertama.warna)

# Memanggil Method
mobil_pertama.klakson()