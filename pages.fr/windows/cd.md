# cd

> Affiche le répertoire de travail courant ou permet de se déplacer vers un autre répertoire.
> Dans PowerShell, cette commande est un alias de `Set-Location`. Cette documentation est basée sur la version `cmd` de `cd`.
> Plus d'informations : <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Affiche la documentation de la commande PowerShell équivalente :

`tldr set-location`

- Affiche le chemin du répertoire courant :

`cd`

- Se déplace dans un répertoire spécifique sur le même disque :

`cd {{chemin\vers\répertoire}}`

- Se déplace dans un répertoire spécifique sur un autre [d]isque :

`cd /d {{C}}:{{chemin\vers\répertoire}}`

- Remonte vers le répertoire parent du répertoire actuel :

`cd ..`

- Se déplace dans le répertoire personnel de l'utilisateur courant :

`cd %userprofile%`

- Se déplace à la racine du disque actuel :

`cd \`
