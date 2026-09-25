# choco outdated

> Vérifie les paquets obsolètes avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/outdated/>.

- Affiche une liste des paquets obsolètes sous forme de tableau :

`choco outdated`

- Ignore les paquets épinglés dans la sortie :

`choco outdated --ignore-pinned`

- Spécifie une source personnalisée à partir de laquelle vérifier les paquets :

`choco outdated {{[-s|--source]}} {{source_url|alias}}`

- Fournit un nom d'utilisateur et un mot de passe pour l'authentification :

`choco outdated {{[-u|--user]}} {{nom_utilisateur}} {{[-p|--password]}} {{mot_de_passe}}`
