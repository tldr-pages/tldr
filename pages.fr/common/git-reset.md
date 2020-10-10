# git reset

> Annuler des commits ou unstage des changements, en rétablissant la HEAD courrante a un état spécifique.
> Si un chemin est passé, il fonctionne comme "unstage"; si un hachage ou une branche de validation est passé, cela fonctionne comme "uncommit".
> Plus d'informations: <https://git-scm.com/docs/git-reset>.

- Effacer toutes les modifications:

`git reset`

- Effacer les modifications de certains fichiers:

`git reset {{path/to/file(s)}}`

- Effacer les modifications sur une portion de fichier:

`git reset -p {{path/to/file}}`

- Annuler le dernier commit, conserver tout les changements sur le système de fichiers local:

`git reset HEAD~`

- Annule les deux derniers commits, en ajoutant leurs modifications à l'index, c'est-à-dire en préparation pour le commit:

`git reset --soft HEAD~2`

- Annule tout changement local non commité (pour anuler seulement les fichiers non suivis voir `git checkout`):

`git reset --hard`

- Rétablit la branche sur un commit spécifié, en effacant tout changement ou commit effectué depuis lors.

`git reset --hard {{commit}}`
