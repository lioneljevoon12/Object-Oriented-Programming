import turtle

class Rumah:
    def __init__(self, warna):
        self.warna = warna

    def kotak(self, x1, y1, x2, y2):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y1)
        turtle.goto(x2, y2)
        turtle.goto(x1, y2)
        turtle.goto(x1, y1)

    def gambar(self):
        turtle.color(self.warna)

        # Badan rumah
        self.kotak(0, 0, 150, -150)

        # Atap
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(75, 75)
        turtle.goto(150, 0)

        # Pintu (nempel di tanah, y=-150)
        turtle.color("brown")
        self.kotak(55, -150, 95, -70)

        # Jendela kiri
        turtle.color("lightblue")
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


rumah1 = Rumah("blue")
rumah1.gambar()

turtle.done()