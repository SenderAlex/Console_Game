class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if other.is_alive():
            other.health -= self.attack_power
            if other.health <= 0:
                other.health = 0
            print(f'{self.name} аттакует {other.name} и теперь у {other.name} здоровья осталось {other.health}')
        else:
            print(f'{other.name} уже мертв')

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game():
    def __init__(self):
        self.player = Hero('Alex', 100, 20)
        self.computer = Hero('Computer', 100, 20)

    def start_game(self):
        while self.player.is_alive() and self.computer.is_alive():

            # начинает аттаковать игрок
            if self.player.is_alive():
                self.player.attack(self.computer)
                if not self.computer.is_alive():
                    break

            # начинает аттаковать компьютер
            if self.computer.is_alive():
                self.computer.attack(self.player)
                if not self.player.is_alive():
                    break

        if self.player.is_alive():
            print(f'{self.player.name} победил')
        else:
            print(f'{self.computer.name} победил')

game = Game()
game.start_game()

