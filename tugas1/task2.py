import turtle


class Rumah:
    def __init__(self, warna):
        self.warna = warna

    def gambar(self):
        turtle.color(self.warna)

        # Badan rumah
        for i in range(4):
            turtle.forward(150)
            turtle.right(90)

        turtle.left(45)
        turtle.forward(106)
        turtle.right(90)
        turtle.forward(106)
        turtle.right(135)


# Object
rumah1 = Rumah("blue")
rumah1.gambar()

turtle.done()