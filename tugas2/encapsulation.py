class Product:
    #method constructor untuk menginisialisasi atribut produk
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self._stok = stok #protected
        self.__harga = harga #private

    #method setter untuk mengubah harga produk
    def set_harga(self, harga):
        self.__harga = harga

    #method getter untuk mengambil harga produk
    def get_harga(self):
        return self.__harga

    #method untuk menampilkan informasi produk
    def outputProduk(self):
        print("Nama: ", self.nama)
        print("Harga: ", self.__harga)
        print("Stok: ", self._stok)

    #method protected untuk menambah stok produk
    def _tambahStok(self, jumlah):
        self._stok = self._stok + jumlah

    #method private untuk mereset stok menjadi 0
    def __resetStok(self):
        self._stok = 0


#membuat object dari class Product
produk = Product("Ayam Geprek caramel", 10000, 15)

#mengambil harga menggunakan getter
print("Harga", produk.get_harga())

#mengubah harga menggunakan setter
produk.set_harga(16000)
print("Harga", produk.get_harga())
print("\n")

#menampilkan informasi produk
produk.outputProduk()

#menambah stok sebanyak 5
produk._tambahStok(5)
print("Jumlah ayam geprek caramel saat ditambah 5 sekarang berjumlah", produk._stok)

#memanggil private method 
produk._Product__resetStok()
print("Stok produk setelah direset adalah", produk._stok)
produk.outputProduk()
print("\n")

#menambah stok sebanyak 10
produk._tambahStok(10)
produk.outputProduk()