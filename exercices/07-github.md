# Exercice 07 — Travailler avec GitHub

**Objectif :** pousser, récupérer et proposer des changements via une Pull Request.

## A. Pousser une branche

1. ```bash
   git switch main
   git pull
   git switch -c ma-contribution
   ```
2. Ajoute une recette à toi dans `src/recettes.txt`, commite.
3. Pousse la branche :
   ```bash
   git push -u origin ma-contribution
   ```

## B. Ouvrir une Pull Request

1. Sur la page GitHub du dépôt, clique sur **Compare & pull request**.
2. Rédige un titre et une description, puis crée la PR.
3. Regarde l'onglet **Files changed**, ajoute un commentaire sur une ligne.
4. Fusionne la PR avec **Merge pull request**.

## C. Récupérer les changements

1. En local :
   ```bash
   git switch main
   git pull
   git log --oneline --graph
   ```
2. Supprime la branche locale : `git branch -d ma-contribution`.

## D. Simuler un changement distant

1. Sur GitHub, modifie directement `README.md` (icône crayon) et commite en ligne.
2. En local, sur `main`, modifie **un autre fichier** et commite.
3. `git push` est refusé. Pourquoi ?
4. `git pull` puis `git push`. Essaie aussi `git pull --rebase` la prochaine fois
   et compare les historiques.
