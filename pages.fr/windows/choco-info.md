# choco info

> Afficher des informations détaillées sur un forfait avec Chocolatey.
> Plus d'informations : <https://chocolatey.org/docs/commands-info>.

- Afficher des informations sur un package spécifique :

`choco info {{paquet}}`

- Afficher les informations pour un package local uniquement :

`choco info {{paquet}} --local-only`

- Spécifier une source personnalisée à partir de laquelle recevoir des informations sur les packages :

`choco info {{paquet}} --source {{source_url|alias}}`

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco info {{paquet}} --user {{nom d'utilisateur}} --password {{mot de passe}}`
