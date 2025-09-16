import numpy as np

ventes = np.random.randint(50, 100)
prix_vente = np.random.uniform(7, 35, ventes)
ventes_finales = ventes * prix_vente
print(ventes_finales.shape)

# print(ventes.round(2))

print("Prix des livres")