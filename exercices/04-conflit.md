# Exercice 04 — Résoudre un conflit

**Objectif :** comprendre et résoudre un conflit de fusion.

Les branches `conflit-a` et `conflit-b` ont **toutes les deux** modifié la
même ligne de `src/recettes.txt` (le temps de cuisson du gâteau). C'est voulu.

## Étapes

1. Récupère les branches si besoin :
   ```bash
   git fetch
   git switch conflit-a
   ```
2. Essaie de fusionner l'autre branche :
   ```bash
   git merge conflit-b
   ```
   Git annonce un **CONFLICT**.
3. Lance `git status` et ouvre `src/recettes.txt`. Tu verras :
   ```
   <<<<<<< HEAD
   (version de conflit-a)
   =======
   (version de conflit-b)
   >>>>>>> conflit-b
   ```
4. Édite le fichier : garde la version que tu veux (ou mélange les deux),
   et **supprime les marqueurs** `<<<<<<<`, `=======`, `>>>>>>>`.
5. Marque le conflit comme résolu et termine :
   ```bash
   git add src/recettes.txt
   git commit
   ```
6. Regarde le graphe : `git log --oneline --graph`.

## Variante

Recommence depuis l'état initial (`git reset --hard origin/conflit-a`),
relance la fusion, et cette fois abandonne-la avec `git merge --abort`.

## Questions

- Pourquoi Git ne peut-il pas choisir tout seul ?
- Que se passerait-il si tu commitais en laissant les marqueurs dans le fichier ?
