# Exercice 09 — Trouver un bug avec `bisect`

**Objectif :** trouver automatiquement le commit qui a introduit un bug.

Sur la branche `bug-cache`, le script `src/calcul.py` fonctionnait au début,
mais il est cassé maintenant. Il y a une dizaine de commits : lequel a introduit le bug ?

## Vérifier le bug

```bash
git switch bug-cache
python3 src/test_calcul.py    # échoue
```

## Recherche manuelle

```bash
git bisect start
git bisect bad                # la version actuelle est cassée
git bisect good main          # main fonctionnait
```

Git te place sur un commit au milieu. Lance le test, puis indique :
`git bisect good` ou `git bisect bad`. Recommence jusqu'à ce que Git
annonce *"... is the first bad commit"*.

Termine avec `git bisect reset`.

## Recherche automatique

```bash
git bisect start bug-cache main
git bisect run python3 src/test_calcul.py
git bisect reset
```

## Questions

- Combien d'étapes a-t-il fallu ? Combien en faudrait-il pour 1000 commits ?
- Quel est le message du commit coupable ? Corrige le bug avec un `revert`.
