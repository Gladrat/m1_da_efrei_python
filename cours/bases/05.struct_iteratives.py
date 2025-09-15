# while(True):
#     pass

# compteur = 1

# while(compteur<=1000):
#     print(compteur)
#     compteur += 1

# [0, 1, 2, 3, 4, 5]

# for i in list(range(10000)):
#     print(i)

# print(list(range(100)))

# arr = []
# for i in range(100):
#     arr.append(i)

# print(arr)

# arr = list(range(100, -1, -1))

# print(arr)

el = ["Camille", "Lisa", "Arnaud", "Jack"]

# for i in range(len(el)):
#     print(f"Eleve n°{i +1:02d}: {el[i]}")

for e in enumerate(el, 100):
    print(f"Eleve n°{e[0]:02d}: {e[1]}")

