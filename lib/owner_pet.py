
class Pet:
    PET_TYPES = ["dog", 
             "cat", 
             "rodent", 
             "bird", 
             "reptile", 
             "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Breed must be in list of approved breeds.")



class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


