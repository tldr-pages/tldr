# choco search

> Recherche un forfait local ou distant avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/search/>.

- Recherche un forfait :

`choco search {{requête}}`

- Recherche un package localement :

`choco search {{requête}} --local-only`

- Inclut uniquement les correspondances exactes dans les résultats :

`choco search {{requête}} {{[-e|--exact]}}`

- Confirme automatiquement toutes les invites :

`choco search {{requête}} {{[-y|--yes]}}`

- Spécifie une source personnalisée dans laquelle rechercher des packages :

`choco search {{requête}} {{[-s|--source]}} {{source_url|alias}}`

- Fournit un nom d'utilisateur et un mot de passe pour l'authentification :

`choco search {{requête}} {{[-u|--user]}} {{nom d'utilisateur}} {{[-p|--password]}} {{mot de passe}}`
