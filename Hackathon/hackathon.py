
import random


class Character:
    all_character = []
    print(f"*WELCOME TO DOG VS CAT*")
    def __init__(self, name, health=100, power=10, speed=5):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed
        Character.all_character.append(self)
        
        
        
    def info(self):
        print(f"* {self.name} *")
        print(f"health: {self.health}")
        print(f"power: {self.power}")
        print(f"speed: {self.speed}")
        return self

    def changehealth(self, amount):
        self.health += amount
        return self

    def attack(self, attackee):
        print(f"{self.name} is attacking {attackee.name}")
        is_successful = attackee.block(self)
        if is_successful:
            attackee.changehealth(-self.power)

    def block(self, attacker=None):
        defence_roll = random.randint(0,30)
        print(f"{self.name} was hit {defence_roll} against a power level of {attacker.power}")
        if defence_roll > self.health:
            return False
        else:
            return True

class Dog(Character):
    def __init__(self, name, health=100, power=10, speed=5):
        super().__init__(name, health, power, speed)

class Cat(Character):
    def __init__(self, name, health=100, power=6, speed=8):
        super().__init__(name, health, power, speed)



player1 = Dog("Migo")
player2 = Cat("Stogie")

player1.attack(player2)
player1.info()
player2.info()

