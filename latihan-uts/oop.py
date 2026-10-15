class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

player = Character("Player", 100)
player.take_damage(30)

print(f"{player.name} has {player.health} health remaining.")
