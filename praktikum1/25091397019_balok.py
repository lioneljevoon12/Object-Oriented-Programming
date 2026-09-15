class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    def luas(self):
        return 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.lebar * self.tinggi) )

panjang = int(input("Masukkan Panjang: "))
lebar = int(input("Masukkan Lebar: "))
tinggi = int(input("Masukkan Tinggi: "))

balok1 = Balok(panjang, lebar, tinggi)

print("Volume Balok adalah: ", balok1.volume())
print("Luas Permukaan Balok adalah", balok1.luas())