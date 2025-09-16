eleves = ["Camille", "Lisa", "Arnaud", "Jack"]

print(eleves[0])

# eleves = []
# eleves = list()

eleves.append("Lucas")

print(len(eleves))

print(eleves[4])
print(eleves[len(eleves)-1])
print(eleves[-1])
print(eleves[-2])
print(eleves[len(eleves) * -1])

# ["Camille", "Lisa", "Arnaud", "Jack"]
#       |       |       |           |
#       0       1       2           3
#      -4      -3      -2          -1

eleves.extend(["el1", "el2"])

eleves += ["el8", "el9"]

print(eleves)

# Slicing

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]

print(jours[3])
print(jours[-4])

# print(jours[7])

print(jours[:5])

print(jours[5:])
print(jours[-2:])

jours_fr_en = [
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
    ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
]

print(jours_fr_en[1][-2:])