class MenuItem:
    def __init__(self, nama, harga, detail):
        self.nama = nama
        self.harga = harga
        self.detail = detail

    def info(self):
        print(self.nama, ": Rp", self.harga, self.detail,)

    def total(self, jumlah):
        total = self.harga * jumlah
        if jumlah > 3:
            total = total * 0.9
        return total


menu = [
    MenuItem("Ayam Geprek", 10000, "450kkal"),
    MenuItem("Rendang", 15000, "700kkal"),
    MenuItem("Soto", 12000, "350kkal"),
    MenuItem("Nasi Goreng", 13000, "340kkal")
]

no = 1

for item in menu:
    print(no, end=". ")
    item.info()
    no += 1

pilihan = int(input("Masukkan pilihan 1-4: "))
jumlah = int(input("Masukkan jumlah: "))

if(pilihan == 1):
    print("Total Harga = ", menu[0].total(jumlah))
elif(pilihan == 2):
    print("Total Harga = ", menu[1].total(jumlah))
elif(pilihan == 3):
    print("Total Harga = ", menu[2].total(jumlah))
elif(pilihan == 4):
    print("Total Harga = ", menu[4].total(jumlah))