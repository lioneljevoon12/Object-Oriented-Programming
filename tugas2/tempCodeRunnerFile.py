produk.set_harga(16000)
print("Harga", produk.get_harga())
print("\n")

produk.outputProduk()

produk._tambahStok(5)
print("Jumlah ayam geprek caramel saat ditambah 5 sekarang berjumlah", produk._stok)

produk._Product__resetStok()
print("Stok produk setelah direset adalah", produk._stok)
produk.outputProduk()
print("\n")

produk._tambahStok(10)
produk.outputProduk()