# choco outdated

> Vérifiez les packages obsolètes avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/outdated/>.

- Afficher une liste des packages obsolètes sous forme de tableau :

`choco outdated`

- Ignorer les packages épinglés dans la sortie :

`choco outdated --ignore-pinned`

- Spécifiez une source personnalisée à partir de laquelle vérifier les packages :

`choco outdated {{[-s|--source]}} {{source_url|alias}}`

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco outdated {{[-u|--user]}} {{nom_d_utilisateur}} {{[-p|--password]}} {{mot_de_passe}}`
