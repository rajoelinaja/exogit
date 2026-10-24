# Exercice 03 — Les branches

**Objectif :** travailler en parallèle puis fusionner.

## Étapes

1. Depuis `main`, crée une branche :
   ```bash
   git switch main
   git switch -c ajout-dessert
   ```
2. Ajoute une recette de dessert à la fin de `src/recettes.txt` et commite.
3. Reviens sur `main` (`git switch main`) : ta recette a disparu du fichier ! Normal ?
4. Visualise : `git log --oneline --graph --all`.
5. Fusionne : `git merge ajout-dessert`.
   Git annonce un **fast-forward**. Que veut dire ce terme ?
6. Maintenant, crée deux branches depuis `main` : `branche-x` et `branche-y`.
   Dans chacune, modifie un **fichier différent** et commite.
7. Sur `main`, fusionne `branche-x` puis `branche-y`.
   Cette fois, Git crée un **commit de fusion**. Regarde le graphe.
8. Supprime les branches fusionnées : `git branch -d branche-x branche-y ajout-dessert`.

## Questions

- Pourquoi la deuxième fusion n'est-elle pas un fast-forward ?
- Que se passe-t-il si tu essaies `git branch -d` sur une branche non fusionnée ?
