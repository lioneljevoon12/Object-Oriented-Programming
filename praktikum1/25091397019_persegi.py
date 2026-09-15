class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

persegi1 = Persegi(5)
print("Persegi 1")
print("Panjang sisi: ", persegi1.sisi)
print("Luas Persegi:", persegi1.luas)
print("Keliling Persegi", persegi1.keliling)
print("\n")

persegi2 = Persegi(10)
print("Persegi 2")
print("Panjang sisi: ", persegi2.sisi)
print("Luas Persegi:", persegi2.luas)
print("Keliling Persegi", persegi2.keliling)
print("\n")

persegi3 = Persegi(15)
print("Persegi 3")
print("Panjang sisi: ", persegi3.sisi)
print("Luas Persegi:", persegi3.luas)
print("Keliling Persegi", persegi3.keliling)
print("\n")