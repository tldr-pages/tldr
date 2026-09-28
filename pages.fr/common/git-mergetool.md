# git mergetool

> Exécute un utilitaire de différences pour résoudre les conflits de merge.
> Plus d'informations : <https://git-scm.com/docs/git-mergetool>.

- Démarre l'outil de différences par défaut :

`git mergetool`

- Liste les outils de différences valides :

`git mergetool --tool-help`

- Démarre l'outil de différences en précisant son nom :

`git mergetool {{[-t|--tool]}} {{tool_name}}`

- Démarre l'outil de différences sans dialogues :

`git mergetool {{[-y|--no-prompt]}}`

- Utilise explicitement l'outil de différences graphique (voir la variable de config `merge.guitool`) :

`git mergetool {{[-g|--gui]}}`

- Utilise explicitement l'outil de différences classique (voir la variable de config `merge.tool`) :

`git mergetool --no-gui`
