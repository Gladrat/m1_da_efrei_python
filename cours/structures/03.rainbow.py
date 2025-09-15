import hashlib
import string
import itertools

def md5_str(texte: str) -> int:
    return hashlib.md5(texte.encode("utf-8")).hexdigest()

print(md5_str("mon secret"))

# Alphabet : majuscules + minuscules
alphabet = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Générer toutes les combinaisons de longueur 3
for combo in itertools.product(alphabet, repeat=3):
    print("".join(combo))