class Mobil:
    #constructor
    def __init__(self, warna, merk):
        self.warna = warna
        self.merk = merk

mobil1 = Mobil("Merah", "Toyota")
print(mobil1.warna) #output: Merah 
print(mobil1.merk) #output: Toyota

print("warna mobil1 adalah", mobil1.warna) #output: warna mobil1 adalah Merah
print("merk mobil1 adalah", mobil1.merk) #output: merk mobil1 adalah Toyota
print("\n")

#objek kedua

mobil2 = Mobil("Biru", "Honda")
print(mobil2.warna) #output: Biru
print(mobil2.merk) #output: Honda


