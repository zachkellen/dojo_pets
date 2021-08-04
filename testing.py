from ninja import Ninja
from pet import Pet
from pet import Dog
from pet import Cat

zach = Ninja('Zach', 'Kellen', 3, 10, 'Duke', 'Dog', 'Sit')

zach.feed().walk().bathe()
# .walk().bathe()
print(zach.pet.name)
print(zach.pet.energy)
print(zach.pet.health)
print(zach.pet.sound)

duke = Dog('Duke', 'Dog', 'Sit')
print(duke.sound)