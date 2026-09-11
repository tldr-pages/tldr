# choco info

> Affiche des informations détaillées sur un forfait avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Affiche des informations sur un package spécifique :

`choco info {{paquet}}`

- Affiche les informations pour un package local uniquement :

`choco info {{paquet}} {{[-l|--local-only]}}`

- Spécifie une source personnalisée à partir de laquelle recevoir des informations sur les packages :

`choco info {{paquet}} {{[-s|--source]}} {{source_url|alias}}`

- Fournit un nom d'utilisateur et un mot de passe pour l'authentification :

`choco info {{paquet}} {{[-u|--user]}} {{nom d'utilisateur}} {{[-p|--password]}} {{mot de passe}}`
