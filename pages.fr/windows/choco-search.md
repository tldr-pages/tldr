# choco search

> Recherchez un forfait local ou distant avec Chocolatey.
> Plus d'information: <https://chocolatey.org/docs/commands-search>.

- Rechercher un forfait :

`choco search {{requête}}`

- Rechercher un package localement :

`choco search {{requête}} --local-only`

- Inclure uniquement les correspondances exactes dans les résultats :

`choco search {{requête}} --exact`

- Confirmer automatiquement toutes les invites :

`choco search {{requête}} --yes`

- Spécifiez une source personnalisée dans laquelle rechercher des packages :

`choco search {{requête}} --source {{source_url|alias}}`

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco search {{requête}} --user {{nom d'utilisateur}} --password {{mot de passe}}`
