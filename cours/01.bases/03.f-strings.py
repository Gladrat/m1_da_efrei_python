mot = "Hello"

prenom = "James"

# print(phrase + " " + prenom)

print(f"{mot}, this is my name: {prenom}.")

version = 3.13

print(f"Python v.{version}")

age = 13

print(f"Alcool: { "Autorisé" if age>=18 else "Interdit" }")

habitants = 7_753_000_000
superficie = 149_000_000

print(f"Nb d'habitants par km²: {round(habitants/superficie, 2)}")
print(f"Nb d'habitants par km²: {habitants/superficie:.2f}")