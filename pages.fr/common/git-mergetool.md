# git mergetool

> Executer un utilitaire de différences pour résoudre les conflits de merge.
> Plus d'informations : <https://git-scm.com/docs/git-mergetool>.

- Démarrer l'outil de différences par défaut :

`git mergetool`

- Lister les outils de différences valides :

`git mergetool --tool-help`

- Démarrer l'outil de différences en précisant son nom :

`git mergetool --tool {{tool_name}}`

- Démarrer l'outil de différences sans dialogues :

`git mergetool --no-prompt`

- Utiliser explicitement l'outil de différences graphique (voir la variable de config `merge.guitool`) :

`git mergetool --gui`

- Utiliser explicitement l'outil de différences classique (voir la variable de config `merge.tool`) :

`git mergetool --no-gui`
