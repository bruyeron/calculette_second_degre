# Calculette Scientifique — Solveur d'Équations du Second Degré

## 1. But du projet
Application permettant de résoudre des équations du second degré de la forme **$ax^2 + bx + c = 0$** avec des coefficients entiers ($a, b, c \in \mathbb{Z}$).
Ce projet met en pratique le travail collaboratif sur GitHub, la revue de code croisée et l'intégration continue (CI/CD).

## 2. Technologies utilisées
- **Logique métier (Backend) :** Python 3 (FastAPI, Uvicorn, Pytest)
- **Interface graphique (Frontend) :** ReactJS
- **Qualité & CI/CD :** Git, GitHub, GitHub Actions (et préparation SonarCloud)

## 3. Répartition des rôles
- **Élève 1 (`feature/interface-eleve1`) :** Développement de l'interface utilisateur ReactJS (saisie des valeurs $a, b, c$ et affichage des résultats).
- **Élève 2 (`feature/calcul-eleve2`) :** Développement du module de calcul mathématique ($\Delta = b^2 - 4ac$ et calcul des racines) et de l'API.

## 4. Consignes de revue de code
Toute fusion vers la branche `main` passe obligatoirement par une Pull Request relue et validée par le binôme selon les critères suivants :
- **Nommage :** Variables, fonctions et fichiers explicites.
- **Séparation des responsabilités :** Logique mathématique isolée de l'affichage/API.
- **Gestion des erreurs :** Prise en compte du cas $a = 0$ et des entrées invalides.
- **Tests & Portabilité :** Code fonctionnel sur les deux environnements sans chemins absolus.