# tableaux associatifs

t: list = [None] * 10

pays: list[str] = ["Afghanistan", "Afrique du Sud", "Allemagne", "Belgique", "Estonie"]
code_pays = ["AF", "ZA", "DE", "BE", "EE"]


def fonction_hachage(val: str)  -> int:
    return sum(ord(car) for car in val)


def generate_key(val, tab):
    return val % len(tab)


print(fonction_hachage("Afghanistan"))
h = fonction_hachage("Afghanistan")
print(generate_key(h, t))
k = generate_key(h, t)

t[k] = "Afghanistan"

print(t)


student = {
    "id": "Geoffroy", "age": 40, "cours": [{"nom": "math", "note": 12}], "vip": True
}