# asdf

> Interface en ligne de commande pour gérer les versions de différents paquets.
> Plus d'informations : <https://asdf-vm.com>.

- Liste toutes les extensions disponibles :

`asdf plugin-list-all`

- Installe une extension :

`asdf plugin-add {{nom}}`

- Liste toutes les versions disponible d'un paquet :

`asdf list-all {{nom}}`

- Installe une version spécifique d'un paquet :

`asdf install {{nom}} {{version}}`

- Fixe au global une version d'un paquet :

`asdf global {{nom}} {{version}}`

- Fix en local la version d'un paquet :

`asdf local {{nom}} {{version}}`
