# git stash

> Mettre les changements locaux de Git dans un endroit temporaire (Le stash).
> Plus d'informations: <https://git-scm.com/docs/git-stash>.

- Mettre les changements courants (sauf ceux provenant de fichiers qui ne sont pas suivi) dans un *stash*:

`git stash [push -m {{message_optionnel_pour_le_stash}}]`

- Mettre les changements courants (incluant les fichiers qui ne sont pas suivi) dans un *stash*:

`git stash -u`

- Selectionner interactivement les parties des fichiers changer à mettre dans un *stash*:

`git stash -p`

- Lister tout les *stash* (Montre le nom du *stash*, la branche reliée et le message):

`git stash list`

- Appliquer un *stash* à la tête git (le dernier stash est celui choisi par défaut, aussi appellé `stash@{0}`):

`git stash apply {{nom_du_stash_ciblé_optionnellement}}`

- Appliquer un *stash* (le dernier *stash* est celui choisi par défaut), et l'enlever de la liste s'il n'y a pas de conflits:

`git stash pop {{message_optionnel_pour_le_stash}}`

- Détruire un *stash* (le dernier *stash* est celui choisi par défaut):

`git stash drop {{message_optionnel_pour_le_stash}}`

- Détruire tout les *stash*:

`git stash clear`
