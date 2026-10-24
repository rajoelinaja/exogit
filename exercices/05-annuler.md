# Exercice 05 — Annuler des erreurs

**Objectif :** connaître les 3 façons principales de revenir en arrière.

Travaille sur une branche à toi : `git switch -c pratique-05`.

## A. Corriger le dernier commit (`--amend`)

1. Crée `notes.txt`, commite avec le message `"Ajout notse"` (faute volontaire).
2. Corrige le message : `git commit --amend -m "Ajout notes"`.
3. Oublie un fichier : crée `oubli.txt`, puis `git add oubli.txt` et
   `git commit --amend --no-edit`. Il est maintenant dans le commit précédent.

## B. Annuler proprement un vieux commit (`revert`)

1. Fais trois commits qui ajoutent chacun une ligne à `notes.txt`.
2. Annule celui du milieu :
   ```bash
   git log --oneline
   git revert <identifiant-du-commit-du-milieu>
   ```
3. Regarde `git log` : l'historique est conservé, un **nouveau** commit annule l'ancien.

## C. Défaire des commits (`reset`)

1. `git reset --soft HEAD~1` → le dernier commit disparaît, ses changements restent indexés.
2. Recommite-les.
3. `git reset --hard HEAD~1` → le commit **et** ses changements disparaissent.
4. Panique contrôlée : retrouve-le avec `git reflog`, puis
   `git reset --hard <identifiant>`.

## Règle d'or

> Sur une branche **déjà partagée** (poussée sur GitHub), utilise `revert`.
> `reset` et `--amend` réécrivent l'historique : réserve-les à ton travail local.
