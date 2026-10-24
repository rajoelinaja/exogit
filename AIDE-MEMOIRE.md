# Aide-mémoire Git

## Observer
| Commande | Rôle |
|---|---|
| `git status` | État des fichiers (modifiés, indexés, non suivis) |
| `git log --oneline --graph --all` | Historique compact de toutes les branches |
| `git diff` | Changements non indexés |
| `git diff --staged` | Changements indexés (prêts à être commités) |
| `git show <commit>` | Détail d'un commit |
| `git reflog` | Tous les déplacements de HEAD (pour récupérer ce qu'on croit perdu) |

## Enregistrer
| Commande | Rôle |
|---|---|
| `git add <fichier>` | Indexer un fichier |
| `git add -p` | Indexer morceau par morceau |
| `git commit -m "message"` | Créer un commit |
| `git commit --amend` | Modifier le dernier commit |

## Branches
| Commande | Rôle |
|---|---|
| `git branch` | Lister les branches |
| `git switch <branche>` | Changer de branche |
| `git switch -c <branche>` | Créer et changer de branche |
| `git merge <branche>` | Fusionner une branche dans la branche courante |
| `git branch -d <branche>` | Supprimer une branche fusionnée |

## Annuler
| Commande | Rôle |
|---|---|
| `git restore <fichier>` | Abandonner les modifications d'un fichier |
| `git restore --staged <fichier>` | Désindexer un fichier |
| `git revert <commit>` | Créer un commit qui annule un autre (sûr, historique conservé) |
| `git reset --soft HEAD~1` | Défaire le dernier commit, garder les changements indexés |
| `git reset --hard HEAD~1` | Défaire le dernier commit ET jeter les changements ⚠️ |

## Distant
| Commande | Rôle |
|---|---|
| `git remote -v` | Voir les dépôts distants |
| `git fetch` | Récupérer sans fusionner |
| `git pull` | Récupérer et fusionner |
| `git push -u origin <branche>` | Pousser une nouvelle branche |

## Divers
| Commande | Rôle |
|---|---|
| `git stash` / `git stash pop` | Mettre de côté / reprendre des modifications |
| `git rebase -i HEAD~n` | Réorganiser les n derniers commits |
| `git bisect start/good/bad` | Recherche dichotomique d'un bug |
