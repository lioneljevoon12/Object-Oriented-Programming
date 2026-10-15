# class Character:
#     pass

#penggunaan class dengan method 

class Character:
    def show_status(self):
        print("Character is alive")

player = Character()
player.show_status()  #output: Character is alive

#penggunaan class dengan atribut

class Karakter:
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print("Character name is", self.name)

player1 = Karakter()
player1.set_name("Player 1")
player1.show_name()  #output: Character name is Player 1

#membuat objek yang berbeda dari satu class
player2 = Karakter()
player2.set_name("Player 2")
player2.show_name()  #output: Character name is Player 2

player3 = Karakter()
player3.set_name("Player 3")
player3.show_name()  #output: Character name is Player 3

#penggunaan class dengan atribut berbeda

class Karakters:
    def set_stats(self, name, health):
        self.name = name
        self.health = health

    def show_stats(self):
        print("Character name is", self.name)
        print("Character health is", self.health)

player4 = Karakters()
player4.set_stats("Player 4", 100)
player4.show_stats()  #output: Character name is Player 4
                       #        Character health is 100

#mengubah atribut melalui method

class Karakters2:
    def set_stats(self, name, health):
        self.name = name
        self.health = health

    def show_stats(self):
        print("Character name is", self.name)
        print("Character health is", self.health)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

player5 = Karakters2()
player5.set_stats("Player 5", 100)

player5.show_stats()  #output: Character name is Player 5
player5.take_damage(30)
player5.show_stats()  #output: Character name is Player 5
                       #        Character health is 70
player5.heal(20)
player5.show_stats()  #output: Character name is Player 5
                       #        Character health is 90

#studi kasus 

class GameCharacter:
    def set_stats(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def show_stats(self):
        print("Character name is", self.name)
        print("Character health is", self.health)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

hero = GameCharacter()
hero.set_stats("Hero", 120)
hero.take_damage(40)

boss = GameCharacter()
boss.set_stats("Boss", 300)
boss.take_damage(75)

hero.show_stats()  #output: Character name is Hero
boss.show_stats()  #output: Character name is Boss

#try method is_alive
if hero.is_alive():
    print(hero.name, "is alive")
    