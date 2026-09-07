class Mobil:
    pass

mobil1 = Mobil()
mobil2 = Mobil()

#Mobil adalah class, sedangkan mobil1 dan mobil2 adalah object dari class Mobil.

#atrribut dan property

class Kucing:
    bulu = "hitam"

kucing1 = Kucing()
print(kucing1.bulu) #output: hitam  

bulu = kucing1.bulu
print("warna bulu kucing1 adalah", bulu) #output: warna bulu kucing1 adalah hitam