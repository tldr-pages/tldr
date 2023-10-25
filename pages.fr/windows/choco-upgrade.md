# choco upgrade

> Surclassez un ou plusieurs forfaits avec Chocolatey.
> Plus d'information: <https://chocolatey.org/docs/commands-upgrade>.

- Mettre à niveau un ou plusieurs packages séparés par des espaces:

`choco upgrade {{paquet1 paquet2 ...}}`

- Mise à niveau vers une version spécifique d'un package:

`choco upgrade {{paquet}} --version {{version}}`

- Mettre à niveau tous les packages:

`choco upgrade all`

- Mettre à niveau tous les packages sauf ceux spécifiés, séparés par des virgules:

`choco upgrade all --except "{{paquet1 paquet2 ...}}"`

- Confirmer automatiquement toutes les invites:

`choco upgrade {{paquet}} --yes`

- Spécifier une source personnalisée à partir de laquelle recevoir les packages:

`choco upgrade {{paquet}} --source {{source_url|alias}}`

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification:

`choco upgrade {{paquet}} --user {{nom d'utilisateur}} --password {{mot de passe}}`
