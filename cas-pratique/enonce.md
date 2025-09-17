## 🎯 Objectif

Votre mission est de concevoir un **rapport de benchmark** évaluant les performances d’un ou plusieurs modèles d’IA sur des questions de culture générale.

L’exercice permet de mettre en œuvre un **pipeline complet** de data ingénierie :

- collecte et intégration de données,
- enrichissement par appel à des modèles d’IA,
- génération et visualisation de résultats.

## 🗂️ Étape 1 : Constitution d’un dataset de questions de culture générale

1. **Source de données** :
    - Utilisez le site [Open Trivia Database (OpenTDB)](https://opentdb.com/), une API publique proposant des milliers de questions catégorisées (science, histoire, divertissement, etc.).
2. **Format du dataset brut** :
    - Conservez les colonnes suivantes :
        - `question` : l’intitulé de la question
        - `category` : la catégorie (ex : Histoire, Sciences, etc.)
        - `difficulty` : niveau de difficulté (facile, moyen, difficile)
        - `correct_answer` : la bonne réponse
        - `incorrect_answers` : les distracteurs proposés
        - `type` : le type de question (multiple ou booléen)
3. **Stockage initial** :
    - Sauvegardez vos données dans un fichier **CSV** (`questions_raw.csv`).

## 🔄 Étape 2 : Module de data intégration & enrichissement avec un modèle d’IA

1. **Prétraitement** :
    - Nettoyez les données si nécessaire.
    - Uniformisez la casse et le formatage des réponses si nécessaire.
2. **Intégration de l’IA avec Ollama** :
    - Installez [Ollama](https://ollama.ai/) (un runtime léger permettant d’exécuter localement des modèles LLM).
    - Téléchargez un modèle adapté à votre machine (par exemple `llama3.2`, `gemma3`, ou tout autre modèle supporté).
    - Utilisez l’**API Python d’Ollama** pour automatiser la génération de réponses IA :
    - Pour chaque question de votre dataset, interrogez le modèle et stockez la réponse générée.
3. **Enrichissement du dataset** :
    - Ajoutez les colonnes suivantes :
        - `ai_answer` : réponse donnée par le modèle
        - `ai_correct` : booléen (`True` si la réponse IA correspond à la bonne réponse)
        - `response_time` : temps de génération mesuré en secondes
    - Exportez le dataset enrichi dans un fichier `benchmark_results.csv`.

## ⚠️ Importance du prompt

Le **prompt** (la façon dont vous posez la question au modèle) influence fortement la qualité des réponses obtenues.

- Une même question peut donner des résultats très différents selon le contexte fourni.
- Exemple :
    - Prompt simple : *"Qui a peint la Joconde ?"*
    - Prompt plus robuste : *"Réponds uniquement par un nom propre. Question : Qui a peint la Joconde ?"*
    - Il existe des versions encore plus optimisées, à vous de les trouver !
- Dans ce cas pratique, il est recommandé de **standardiser les prompts** pour que le benchmark soit cohérent.
- Vous pouvez tester plusieurs variantes de prompt afin d’observer leur impact sur :
    - le **taux de bonnes réponses**,
    - la **longueur et précision** des réponses,
    - la **robustesse** face aux ambiguïtés.

Pour un benchmark rigoureux, vous pouvez garder une trace de la formulation du prompt dans votre dataset (`prompt_version`).

## 📊 Étape 3 : Rapport de benchmark

Vous allez produire un **rapport d’analyse des résultats** afin de comparer les performances du modèle.

### Analyses possibles

- **Performance globale** : taux de bonnes réponses (%)
- **Par catégorie** : précision par thème (histoire, sciences, etc.)
- **Par niveau de difficulté** : facile vs difficile
- **Par temps de réponse** : rapidité moyenne par question
- **Comparaison de modèles** (optionnel) : exécutez le benchmark avec plusieurs modèles disponibles via Ollama (`llama2`, `mistral`, etc.) et comparez leurs performances.

### Méthodes de restitution

1. **Notebook** :
    - Utilisez **Pandas** pour manipuler les données.
    - Utilisez **Matplotlib** ou **Seaborn** pour créer des visualisations :
        - histogrammes de précision,
        - courbes de temps de réponse,
        - heatmaps par catégorie et difficulté.
2. **Application interactive** :
    - Vous pouvez aller plus loin en utilisant **Streamlit** :
        - Chargement dynamique du dataset enrichi,
        - Tableaux filtrables,
        - Graphiques interactifs,
        - Comparaison entre plusieurs modèles.

## 📦 Livrables attendus

Créez un dépôt Github contenant :

0. **Script de scraping**
1. **Dataset brut** (`questions_raw.csv`)
2. **Dataset enrichi** (`benchmark_results.csv`)
3. **Notebook d’analyse** (`benchmark_analysis.ipynb`)
OU
3. **Application Streamlit/Dash** pour un rapport interactif