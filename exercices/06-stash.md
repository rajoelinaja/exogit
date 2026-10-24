# Exercice 06 — Mettre de côté avec `stash`

**Objectif :** changer de tâche sans commiter un travail inachevé.

## Scénario

Tu modifies une recette quand on te demande une correction urgente sur `main`.

## Étapes

1. Crée une branche `pratique-06`, modifie `src/recettes.txt` **sans commiter**.
2. Essaie `git switch main`. Selon les cas Git refuse ou emporte tes modifications.
3. Mets ton travail de côté :
   ```bash
   git stash push -m "recette en cours"
   git status   # tout est propre
   ```
4. Va sur `main`, fais une petite correction dans `README.md`, commite.
5. Reviens : `git switch pratique-06`.
6. Liste et récupère :
   ```bash
   git stash list
   git stash pop
   ```

## Bonus

- Fais deux `stash` différents, puis récupère le plus ancien avec `git stash apply stash@{1}`.
- Que fait `git stash -u` de plus que `git stash` ?
