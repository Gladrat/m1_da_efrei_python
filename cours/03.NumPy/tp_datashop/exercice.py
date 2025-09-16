import numpy as np

# Ex 1
# np.random.seed(0)
ventes = np.random.randint(0, 1001, (12, 5))
print(ventes)

# Ex 2
moyenne_ventes_produit = ventes.mean(axis=0).round()
print(moyenne_ventes_produit)

# Ex 3
# print(np.where(ventes[:, 0] > moyenne_ventes_produit[0]))
print(np.where(ventes[:, 0] > moyenne_ventes_produit[0]))
print(np.where(ventes[:, 0] > moyenne_ventes_produit[0])[0] + 1)

# Ex 4
mois_p2_mieux_p3 = np.where(ventes[:, 1] > ventes[:, 2])
print(mois_p2_mieux_p3)

# Ex 5
total_vente_par_produit = np.sum(ventes, axis=0)
print(total_vente_par_produit)
print(np.max(total_vente_par_produit))
print(np.argmax(total_vente_par_produit))

# Ex 6
print(ventes)
mois_ventes_faibles = np.all(ventes < 500, axis=1)
print(mois_ventes_faibles)

exit()

# Ex 7
augmentation_ventes = np.diff(ventes, axis=0) > 0
print(augmentation_ventes)
print(augmentation_ventes.shape)

# Ex 8
# variations_ventes = np.diff(ventes, axis=0) / ventes[:-1] * 100
# ventes.mean(axis=0)

# print(np.argmax(np.mean(np.diff(ventes, axis=0), axis=0)))
# print(np.argmin(np.mean(np.diff(ventes, axis=0), axis=0)))

print(np.diff(ventes, axis=0))


# Ex 9
moyennes = np.mean(ventes, axis=0)
print(moyennes)

moyennes_sup = ventes > moyennes
print(moyennes_sup)

ventes_sup_moyennes_mois = np.sum(moyennes_sup, axis=1)
print(ventes_sup_moyennes_mois)

print(np.where(ventes_sup_moyennes_mois >= 3))