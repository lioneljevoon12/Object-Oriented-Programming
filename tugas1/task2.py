import turtle

turtle.speed(0)      # gambar secepat mungkin
turtle.hideturtle()  # sembunyikan kursor kura-kura

# Fungsi Bantu
def lingkaran(cx, cy, r, warna_garis, warna_isi):
    """Gambar lingkaran dengan pusat (cx, cy) dan jari-jari r."""
    turtle.penup()
    turtle.setheading(0)          # WAJIB arah 0, pusat lingkaran
    turtle.goto(cx, cy - r)       # turtle.circle() mulai dari titik paling bawah
    turtle.pendown()
    turtle.color(warna_garis, warna_isi)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


class Rumah:
    def __init__(self, warna):
        self.warna = warna

    def kotak(self, x1, y1, x2, y2):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.begin_fill()        # mulai isi warna
        turtle.goto(x2, y1)
        turtle.goto(x2, y2)
        turtle.goto(x1, y2)
        turtle.goto(x1, y1)
        turtle.end_fill()          # selesai isi warna

    def gambar(self):
        # Badan rumah: garis = warna rumah, isi = kuning muda
        turtle.color(self.warna, "lightyellow")
        self.kotak(0, 0, 150, -150)

        # Atap: segitiga merah
        turtle.color("darkred", "red")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(75, 75)
        turtle.goto(150, 0)
        turtle.goto(0, 0)
        turtle.end_fill()

        # Pintu (nempel di tanah, y=-150)
        turtle.color("saddlebrown", "brown")
        self.kotak(55, -150, 95, -70)

        # Jendela kiri: garis hitam, isi biru muda
        turtle.color("black", "lightblue")
        self.kotak(20, -60, 55, -95)
        turtle.penup()
        turtle.goto(37.5, -60)
        turtle.pendown()
        turtle.goto(37.5, -95)

        # Jendela kanan
        self.kotak(95, -60, 130, -95)
        turtle.penup()
        turtle.goto(112.5, -60)
        turtle.pendown()
        turtle.goto(112.5, -95)


class Pohon:
    def __init__(self, x, y, ukuran=1, warna_daun="forestgreen"):
        self.x = x                    # posisi tengah batang
        self.y = y                    # posisi tanah (dasar batang)
        self.ukuran = ukuran          # 1 = normal, 1.5 = lebih besar, dst
        self.warna_daun = warna_daun

    def gambar(self):
        u = self.ukuran

        # Batang: kotak coklat
        turtle.color("saddlebrown", "sienna")
        turtle.penup()
        turtle.goto(self.x - 12 * u, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(self.x + 12 * u, self.y)
        turtle.goto(self.x + 12 * u, self.y + 70 * u)
        turtle.goto(self.x - 12 * u, self.y + 70 * u)
        turtle.goto(self.x - 12 * u, self.y)
        turtle.end_fill()

        # Daun: 3 lingkaran hijau yang saling numpuk
        lingkaran(self.x, self.y + 110 * u, 45 * u, "darkgreen", self.warna_daun)       # atas
        lingkaran(self.x - 32 * u, self.y + 85 * u, 35 * u, "darkgreen", self.warna_daun)  # kiri
        lingkaran(self.x + 32 * u, self.y + 85 * u, 35 * u, "darkgreen", self.warna_daun)  # kanan


class Langit:
    def __init__(self, warna="lightskyblue"):
        self.warna = warna

    def matahari(self, x, y, r):
        # Sinar: 12 garis di sekeliling matahari (tiap 30 derajat)
        turtle.color("orange")
        for sudut in range(0, 360, 30):
            turtle.penup()
            turtle.goto(x, y)
            turtle.setheading(sudut)
            turtle.forward(r + 8)     # mulai sedikit di luar lingkaran
            turtle.pendown()
            turtle.forward(22)        # panjang sinar
        # Badan matahari
        lingkaran(x, y, r, "orange", "yellow")

    def awan(self, x, y):
        # Awan = 4 lingkaran putih yang saling numpuk
        lingkaran(x, y, 25, "white", "white")
        lingkaran(x + 30, y + 12, 32, "white", "white")
        lingkaran(x + 65, y, 25, "white", "white")
        lingkaran(x + 32, y - 8, 25, "white", "white")

    def gambar(self):
        turtle.bgcolor(self.warna)    # warna latar = warna langit
        self.matahari(-300, 250, 45)
        self.awan(-120, 220)
        self.awan(120, 190)


class Tanah:
    def gambar(self):
        turtle.color("darkgreen", "limegreen")
        turtle.penup()
        turtle.goto(-500, -150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(500, -150)        
        turtle.goto(500, -400)
        turtle.goto(-500, -400)
        turtle.goto(-500, -150)
        turtle.end_fill()


langit = Langit()
langit.gambar()

tanah = Tanah()
tanah.gambar()

pohon1 = Pohon(250, -150)
pohon1.gambar()

pohon2 = Pohon(-120, -150, ukuran=1.3, warna_daun="green")
pohon2.gambar()

rumah1 = Rumah("blue")
rumah1.gambar()

turtle.done()