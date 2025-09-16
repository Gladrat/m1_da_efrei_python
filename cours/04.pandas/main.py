from __future__ import annotations


class Voiture:
    def __init__(self, vin):
        self.couleur = "rouge"
        self.roues = 4
        self.vin = vin

    def demarrer(self):
        pass

    def freiner(self):
        pass

    def klaxonner(self):
        print("Tut tut")

    # def comparer_voiture(self, autre_voiture: Voiture):
    #     return autre_voiture.vin == self.vin

    def __eq__(self, value: Voiture):
        return value.vin == self.vin

    def __gt__(self):
        pass

    def __str__(self):
        return f"C'est une voiture (numéro VIN: {self.vin})"
    
    def __repr__(self):
        return self.__str__()


voiture1 = Voiture(999)
voiture2 = Voiture(999)

print(voiture1 == voiture2)

# print(id(voiture1))
# print(id(voiture2))

# print(voiture1)

# l = [Voiture(0), Voiture(1)]
# print(l)