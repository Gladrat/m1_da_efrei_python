import numpy as np

tab_1d = np.array([1, 2, 3, 4, 5])
print(tab_1d)
print(tab_1d.ndim)

tab_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(tab_2d)
print(tab_2d.ndim)


print(tab_2d[2, 3])
print(tab_2d.shape)

# JAMAIS LE FAIRE - SAUF SI IL N'Y A PAS D'AUTRE SOLUTION
# for ligne in tab_2d:
#     for col in ligne:
#         print(col)

# ---

arr = np.zeros(10)
print(arr)

arr_one = np.ones(10)
print(arr_one)

arr_one = arr_one.astype(int)
print(arr_one)
arr_one = arr_one.astype(str)

arr_div = np.full((10, 3), 5)
print(arr_div)

arr_rnd = np.random.randint(10, 100, (1, 5))
print(arr_rnd)

# Slicing

np.random.seed(0)

arr_rnd = np.random.randint(10, 100, (2, 10))
arr_rnd2 = np.random.randint(10, 100, (2, 10))
# print(arr_rnd)

# print(arr_rnd[:, -2:])
# print(arr_rnd * 100 / 3 + 1 ** 2)

# print(arr_rnd.T)

print(arr_rnd)
print(arr_rnd2)

print(arr_rnd * arr_rnd2)

print(np.min(arr_rnd))
print(np.sum(arr_rnd))
print(np.mean(arr_rnd))
print(np.median(arr_rnd))
print(np.std(arr_rnd))
# print(np.mode(arr_rnd))