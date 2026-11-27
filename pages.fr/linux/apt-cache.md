# apt-cache

> Outil de recherche de paquets Debian et Ubuntu.
> Plus d'informations : <https://manned.org/apt-cache>.

- Recherche un paquet dans vos sources actuelles :

`apt-cache search {{query}}`

- Affiche des informations sur un paquet :

`apt-cache show {{paquet}}`

- Indique si un paquet est installé et à jour :

`apt-cache policy {{paquet}}`

- Affiche les dépendances d'un paquet :

`apt-cache depends {{paquet}}`

- Affiche les paquets qui dépendent d'un paquet particulier :

`apt-cache rdepends {{paquet}}`
