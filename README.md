# exogit — S'entraîner à Git

Dépôt d'exercices progressifs pour pratiquer Git en ligne de commande.
Chaque exercice est dans `exercices/` et se fait directement dans ce dépôt.

## Préparation

```bash
git clone https://github.com/rajoelinaja/exogit.git
cd exogit
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
```

## Les exercices

| # | Thème | Fichier |
|---|-------|---------|
| 01 | Premiers commits (`add`, `commit`, `status`, `log`) | [exercices/01-premiers-commits.md](exercices/01-premiers-commits.md) |
| 02 | Voir les différences (`diff`, `show`, `restore`) | [exercices/02-diff-restore.md](exercices/02-diff-restore.md) |
| 03 | Branches (`branch`, `switch`, `merge`) | [exercices/03-branches.md](exercices/03-branches.md) |
| 04 | Résoudre un conflit de fusion | [exercices/04-conflit.md](exercices/04-conflit.md) |
| 05 | Annuler des erreurs (`revert`, `reset`, `commit --amend`) | [exercices/05-annuler.md](exercices/05-annuler.md) |
| 06 | Mettre de côté (`stash`) | [exercices/06-stash.md](exercices/06-stash.md) |
| 07 | Travailler avec GitHub (`push`, `pull`, Pull Request) | [exercices/07-github.md](exercices/07-github.md) |
| 08 | Réécrire l'historique (`rebase -i`) | [exercices/08-rebase.md](exercices/08-rebase.md) |
| 09 | Retrouver un bug (`bisect`) | [exercices/09-bisect.md](exercices/09-bisect.md) |

Un aide-mémoire est dans [AIDE-MEMOIRE.md](AIDE-MEMOIRE.md).

## Branches préparées

Certaines branches existent déjà pour les exercices :

- `conflit-a` et `conflit-b` → exercice 04
- `historique-brouillon` → exercice 08
- `bug-cache` → exercice 09

Liste-les avec `git branch -a`.

## Conseil

Lance `git status` et `git log --oneline --graph --all` très souvent :
ce sont tes deux meilleurs amis pour comprendre ce qui se passe.
Si tu casses tout, pas de panique : `git reflog` garde la trace de presque tout.
