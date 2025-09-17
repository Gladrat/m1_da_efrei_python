# 📂 Contexte

Le pôle marketing vous a confié un jeu de données clients (`us_customers.csv`) contenant des informations extraites de différentes sources. Ce fichier contient des incohérences, des valeurs manquantes et doit être nettoyé avant intégration dans un outil de data-marketing.

# 🛠️ Contraintes techniques

- Utilisez une version optimisée et moderne des instructions Pandas (regex, etc.)
- Les boucles **python** sont interdites

# 🎯 Objectifs

1. Charger le dataset
2. Effectuer une déduplication des données
3. Supprimer la ou les colonnes inutiles
4. Supprimer les espaces vides avant et après chaque item
5. Identifier les lignes qui contiennent au moins une cellule de type `object` ou `string` malformée (3 résultats)
    1. Converser uniquement les lignes qui ne contiennent pas de cellule maformée
6. Transformer la colonne `Phone_Number`
    1. Format attendu : `(xxx) xxx - xxxx`
    2. Les numéros malformés doivent être transformés en `0000000000`
7. Exploser logiquement la colonne `Address` lorsque c’est possible
8. Adopter une logique de respect du RPGD sur `Tel_opt_in`
    1. Normaliser les valeurs d’opt-in et opt-out avec `Y` ou `N`
    2. Tout ce qui n’est pas expressément opt-in est opt-ou
    3. Tout numéro de téléphone malformé est considéré comme opt-out
9. Adapter cette même logique sur `Newsletter_opt_in`