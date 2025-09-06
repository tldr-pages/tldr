# usermod

> Modifie le compte d'un utilisateur.
> Voir aussi `users`, `useradd`, `userdel`.
> Plus d'informations : <https://manned.org/usermod>.

- Change le nom d'un utilisateur :

`sudo usermod {{[-l|--login]}} {{nouveau_nom}} {{nom_utilisateur}}`

- Modifie l'identifiant numérique d'un utilisateur :

`sudo usermod {{[-u|--uid]}} {{identifiant}} {{nom_utilisateur}}`

- Change le shell d'un utilisateur :

`sudo usermod {{[-s|--shell]}} {{chemin/vers/shell}} {{nom_utilisateur}}`

- Ajoute l'utilisateur à des groupes supplémentaires (attention à l'omission d'espaces) :

`sudo usermod {{[-a|--append]}} {{[-G|--groups]}} {{groupe1,groupe2,...}} {{nom_utilisateur}}`

- Change le répertoire personnel d'un utilisateur et déplace ses fichiers vers celui-ci :

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{chemin/vers/nouveau_répertoire}} {{nom_utilisateur}}`
