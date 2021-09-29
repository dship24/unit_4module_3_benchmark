class DogBoarder:

    def __init__(self, slots, rate):
        self.total_slots = int(slots)
        self.daily_rate = int(rate)
        self.dogs = []

    def is_full(self):
        if self.slots_occupied() == self.total_slots:
            return True
        return False

    def slots_occupied(self):
        total_dogs = 0
        for dog in self.dogs:
            total_dogs += 1
        return total_dogs

    def dog_in_dogs(self, name, breed, owner):
        for dog in self.dogs:
            if dog.name == name and dog.breed == breed and dog.owner == owner:
                return True
        return False

    def board(self, name, breed, owner):
        if self.is_full() == True:
            raise ValueError
        else:
            if self.dog_in_dogs(name, breed, owner) == True:
                raise ValueError
            else:
                self.dogs.append(Dog(name, breed, owner))

    def pick_up(self, name, breed, owner, time):
        if self.dog_in_dogs(name, breed, owner) == True:
            for dog in self.dogs:
                if dog.name == name and dog.breed == breed and dog.owner == owner:
                    self.dogs.remove(dog)
            return self.daily_rate*time
        else:
            raise ValueError

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner