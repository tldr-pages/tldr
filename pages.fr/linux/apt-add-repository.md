# apt-add-repository

> Gère la définition des dépôts apt.
> Plus d'informations : <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Ajout d'un nouveau dépôt :

`apt-add-repository {{repository_spec}}`

- Suppression d'un dépôt :

`apt-add-repository --remove {{repository_spec}}`

- Mise à jour du cache des paquets après ajout d'un dépôt :

`apt-add-repository --update {{repository_spec}}`

- Activation pour les paquets source :

`apt-add-repository --enable-source {{repository_spec}}`
