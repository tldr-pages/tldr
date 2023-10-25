# choco uninstall

> Désinstallez un ou plusieurs packages avec Chocolatey.
> Plus d'information: <https://chocolatey.org/docs/commands-uninstall>.

- Désinstaller un ou plusieurs packages séparés par des espaces:

`choco uninstall {{paquet1 paquet2 ...}}`

- Désinstaller une version spécifique d'un package:

`choco uninstall {{paquet}} --version {{version}}`

- Confirmer automatiquement toutes les invites:

`choco uninstall {{paquet}} --yes`

- Supprimez toutes les dépendances lors de la désinstallation:

`choco uninstall {{paquet}} --remove-dependencies`

- Désinstaller tous les packages:

`choco uninstall all`
