from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, p_name, p_type, p_trick):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(p_name, p_type, p_trick)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        self.pet_food -= 1
        return self

    def bathe(self):
        self.pet.noise()
        return self

# class Pet:
#     def __init__(self, name, type, tricks):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.energy = 50
#         self.health = 100
#         self.sound = "I don't know what I am yet"

#     def sleep():
#         self.energy += 25

#     def eat():
#         self.energy += 5
#         self.health += 10
    
#     def play():
#         self.health += 5

#     def noise():
#         print(self.sound)

# # zach = Ninja('Zach', 'Kellen', 3, 10, 'Duke')
# # print(zach.first_name)