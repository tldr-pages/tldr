# cd

> Affiche le répertoire de travail actuel ou permet de se déplacer vers un autre répertoire.
> Dans PowerShell, cette commande est un alias de `Set-Location`. Cette documentation est basée sur la version `cmd` de `cd`.
> Plus d’informations : <https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/cd>.

- Voir la documentation de la commande PowerShell équivalente :

`tldr set-location`

- Afficher le chemin du répertoire actuel :

`cd`

- Aller dans un répertoire spécifique sur le même disque :

`cd {{chemin\vers\répertoire}}`

- Aller dans un répertoire spécifique sur un autre [d]isque :

`cd /d {{C}}:{{chemin\vers\répertoire}}`

- Remonter vers le répertoire parent du répertoire actuel :

`cd ..`

- Aller dans le répertoire personnel de l’utilisateur courant :

`cd %userprofile%`

- Aller à la racine du disque actuel :

`cd \`
