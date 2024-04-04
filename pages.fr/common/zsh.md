# zsh

> Z SHell, un interpréteur de ligne de commande compatible avec Bash.
> Voir aussi `histexpand` pour l'expansion de l'historique.
> Plus d'informations : <https://www.zsh.org>.

- Démarre une session shell interactive :

`zsh`

- Exécute une commande, puis termine la session :

`zsh -c "{{commande}}"`

- Exécute un script :

`zsh {{chemin/vers/script.zsh}}`

- Exécute un script en affichant chaque commande avant de l'exécuter :

`zsh --xtrace {{chemin/vers/script.zsh}}`

- Démarre une session shell interactive en mode verbeux, qui affiche chaque commande avant de l'exécuter :

`zsh --verbose`

- Exécute une commande spécifique dans Zsh sans motifs génériques d'expansion des noms de fichier :

`noglob "{{command}}"`
