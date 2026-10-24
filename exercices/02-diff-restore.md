# Exercice 02 — Voir et annuler des modifications

**Objectif :** savoir ce qui a changé et revenir en arrière sur un fichier.

## Étapes

1. Ouvre `src/recettes.txt` et change la quantité de farine.
2. Regarde le changement : `git diff`.
3. Indexe le fichier (`git add src/recettes.txt`), puis relance `git diff`.
   Le résultat est vide : pourquoi ? Essaie `git diff --staged`.
4. Désindexe-le : `git restore --staged src/recettes.txt`.
5. Annule complètement ta modification : `git restore src/recettes.txt`.
   Vérifie avec `git status` que tout est propre.
6. Affiche le détail du tout premier commit du dépôt :
   ```bash
   git log --oneline --reverse | head -1
   git show <identifiant>
   ```
7. Compare deux commits : `git diff HEAD~3 HEAD`.

## Questions

- Que signifie `HEAD` ? Et `HEAD~2` ?
- Quelle commande montre qui a modifié chaque ligne d'un fichier ?
  (indice : `git blame`)
