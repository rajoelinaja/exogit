# Exercice 01 — Premiers commits

**Objectif :** comprendre le cycle *modifier → indexer → commiter*.

## Étapes

1. Crée une branche de travail pour toi :
   ```bash
   git switch -c pratique-01
   ```
2. Crée un fichier `moi.txt` contenant ton prénom.
3. Lance `git status`. Le fichier apparaît comme **non suivi** (*untracked*).
4. Indexe-le : `git add moi.txt`, puis relance `git status`. Que remarques-tu ?
5. Commite : `git commit -m "Ajoute moi.txt"`.
6. Ajoute une deuxième ligne à `moi.txt` (ta ville par exemple), puis fais un deuxième commit.
7. Ajoute un fichier `loisirs.txt` et fais un troisième commit.
8. Affiche l'historique :
   ```bash
   git log
   git log --oneline
   ```

## Questions

- Quelle est la différence entre un fichier *modifié* et un fichier *indexé* ?
- Que se passe-t-il si tu fais `git commit` sans avoir fait `git add` ?
- À quoi correspond la longue suite de caractères affichée par `git log` ?

## Bonus

Crée un fichier `.gitignore` contenant `*.log`, puis crée `test.log`.
Est-ce que `git status` le voit ?
