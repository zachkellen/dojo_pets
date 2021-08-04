class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 100
        self.sound = "What is the meaning of life?"

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
        print("No longer hungry")
    
    def play(self):
        self.health += 5
        print("That was fun!")

    def noise(self):
        print(self.sound)

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.energy = 500
        self.health = 200
        self.sound  = "Woof"

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.energy = 1
        self.health = 7
        self.sound  = "Meow"