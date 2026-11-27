# choco upgrade

> Surclasse un ou plusieurs forfaits avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/upgrade/>.

- Met à niveau un ou plusieurs paquets séparés par des espaces :

`choco upgrade {{paquet1 paquet2 ...}}`

- Met à niveau vers une version spécifique d'un paquet :

`choco upgrade {{paquet}} --version {{version}}`

- Met à niveau tous les paquets :

`choco upgrade all`

- Met à niveau tous les paquets sauf ceux spécifiés, séparés par des virgules :

`choco upgrade all --except "{{paquet1 paquet2 ...}}"`

- Confirme automatiquement toutes les invites :

`choco upgrade {{paquet}} {{[-y|--yes]}}`

- Spécifie une source personnalisée à partir de laquelle recevoir les paquets :

`choco upgrade {{paquet}} {{[-s|--source]}} {{source_url|alias}}`

- Fournit un nom d'utilisateur et un mot de passe pour l'authentification :

`choco upgrade {{paquet}} {{[-u|--user]}} {{nom_utilisateur}} {{[-p|--password]}} {{mot_de_passe}}`
