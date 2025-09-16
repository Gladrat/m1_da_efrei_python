import numpy as np

tab_A = np.array([[1,2], [3, 4]])
print(tab_A)

# print(tab_A == 2)
# print(np.logical_or(tab_A == 2, tab_A == 4))
# print(np.logical_and(tab_A > 1, tab_A <= 4))

# filtre = [[True, False], [False, True]]
# print(tab_A[[[True, False], [False, True]]])

rnd_A = np.random.randint(0, 100, (10, 10))
print(rnd_A)
print(rnd_A[rnd_A > 50])

positions = np.where(rnd_A > 50)
print(positions)

print(rnd_A[([2, 5], [0, 0])])

# np.all()
# np.any()

ventes_semaines = np.random.randint(0, 200, 7)
print(ventes_semaines)
print(np.diff(ventes_semaines))