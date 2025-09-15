# def afficher_hello():
#     print("Hello !")

# def generer_hello(name):
#     result = f"Hello {name}"
#     return result


# print(generer_hello("Geoffroy"))

# print(afficher_hello)

# c = afficher_hello

# print(c())

# print(id(c))
import datetime

print("Bonjour", "comment", "tu", "vas", "?")

p = print
def print(val):
    p(f"{datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} {val}")


print("Bonjour", "")
