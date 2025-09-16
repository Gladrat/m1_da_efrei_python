import hashlib
import string
import itertools


def md5_str(texte: str) -> int:
    return hashlib.md5(texte.encode("utf-8")).hexdigest()


alphabet = string.ascii_letters

with open("./password.txt", "w") as file:
    for combo in itertools.product(alphabet, repeat=3):
        line = f"{md5_str("".join(combo))}:{"".join(combo)}\n"
        file.write(line)

print(md5_str("995"))

# chaine (3 reduce) : aaa
    # hash final : 2bcab9d935d219641434683dd9d18a03
