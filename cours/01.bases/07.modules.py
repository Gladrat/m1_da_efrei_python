import random
# import secrets
# import datetime
# import http
# import this
# import math

# import statistics

# print(statistics.mean([1, 2, 3, 4, 4]))

# print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# random.seed(999)

# res = random.randint(0, 100)
# print(res)

# eleves = ["Camille", "Lisa", "Arnaud", "Jack"]
# print(random.choice(eleves))

# for i in range(0, 10):
#     print(random.randint(0, 100))

t = []

for i in range(1_000_0000):
    t.append(random.randint(1, 100))

print(t)