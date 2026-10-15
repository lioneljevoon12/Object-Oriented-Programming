#membuat constuctor dengan __init__ method

class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

nando = GameCharacter("Nando", 100)

#disini memanggil atribut name dan health dari object nando lewat variabel
nama = nando.name
nyawa = nando.health
print("Character name is", nama)  #output: Character name is Nando
print("Character health is", nyawa)  #output: Character health is 100

#langsung memanggil atribut name dan health dari object nando lewat object itu sendiri
print("Character name is", nando.name)  #output: Character name is Nando
print("Character health is", nando.health)  #output: Character health is 100

