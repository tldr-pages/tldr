# chsh

> Change le shell de connexion de l'utilisateur.
> Fait partie de `util-linux`.
> Plus d'informations : <https://manned.org/chsh>.

- Change le shell de connexion de l'utilisateur actuel de manière interactive :

`chsh`

- Liste les shells disponibles :

`chsh {{[-l|--list-shells]}}`

- Change le shell de connexion de l'utilisateur actuel :

`chsh {{[-s|--shell]}} {{chemin/vers/shell}}`

- Change le shell de connexion pour un utilisateur donné :

`sudo chsh {{[-s|--shell]}} {{chemin/vers/shell}} {{nom_utilisateur}}`
