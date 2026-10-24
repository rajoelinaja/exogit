# Exercice 08 — Nettoyer l'historique avec `rebase -i`

**Objectif :** transformer un historique brouillon en historique propre.

La branche `historique-brouillon` contient des commits mal nommés,
des corrections de fautes séparées et un commit inutile. Regarde-les :

```bash
git switch historique-brouillon
git log --oneline main..historique-brouillon
```

## Étapes

1. Lance le rebase interactif sur ces commits :
   ```bash
   git rebase -i main
   ```
2. Dans l'éditeur, tu peux remplacer `pick` par :
   - `reword` (`r`) : changer le message
   - `squash` (`s`) : fusionner avec le commit précédent
   - `fixup` (`f`) : fusionner en jetant le message
   - `drop` (`d`) : supprimer le commit
   - ou changer l'ordre des lignes
3. Objectif : n'obtenir que **2 commits** propres :
   - `Ajoute la recette des crêpes`
   - `Ajoute la recette du smoothie`
4. Vérifie avec `git log --oneline main..HEAD`.

## Si ça tourne mal

```bash
git rebase --abort          # pendant le rebase
git reflog                  # après, pour retrouver l'état d'avant
```

## Bonus

Rebase ta branche sur `main` à jour avec `git rebase main`, puis fusionne-la
dans `main` : la fusion sera un fast-forward. Pourquoi ?
