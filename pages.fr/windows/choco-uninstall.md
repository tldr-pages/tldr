# choco uninstall

> Désinstalle un ou plusieurs paquets avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/choco/commands/uninstall/>.

- Désinstalle un ou plusieurs paquets séparés par des espaces :

`choco uninstall {{paquet1 paquet2 ...}}`

- Désinstalle une version spécifique d'un paquet :

`choco uninstall {{paquet}} --version {{version}}`

- Confirme automatiquement toutes les invites :

`choco uninstall {{paquet}} {{[-y|--yes]}}`

- Supprime toutes les dépendances lors de la désinstallation :

`choco uninstall {{paquet}} {{[-x|--remove-dependencies]}}`

- Désinstalle tous les paquets :

`choco uninstall all`
