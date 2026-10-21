class Enemy:
    def __init__(self, name, hp, attack_point):
        self.name = name
        self.hp = hp
        self.attack_point = attack_point

    def attack(self):
        print(f"{self.name} menyerang dengan kekuatan {self.attack_point}")


class Zombie(Enemy):
    def walk(self):
        print(f"{self.name} berjalan terseok-seok")


class Pocong(Enemy):
    def jump(self):
        print(f"{self.name} melompat-lompat")


class Burung(Enemy):
    def fly(self):
        print(f"{self.name} terbang di udara")

    def walk(self):
        print(f"{self.name} berjalan di tanah")

    def jump(self):
        print(f"{self.name} melompat kecil")


# Membuat objek
zombie1 = Zombie("Zombie", 100, 15)
pocong1 = Pocong("Pocong", 80, 20)
burung1 = Burung("Burung", 50, 10)

# Zombie
print(f"HP {zombie1.name}: {zombie1.hp}")
zombie1.attack()
zombie1.walk()

print("-" * 30)

# Pocong
print(f"HP {pocong1.name}: {pocong1.hp}")
pocong1.attack()
pocong1.jump()

print("-" * 30)

# Burung
print(f"HP {burung1.name}: {burung1.hp}")
burung1.attack()
burung1.fly()
burung1.walk()
burung1.jump()