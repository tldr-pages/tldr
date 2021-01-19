# apt-cache

> Outil de recherche de paquets Debian et Ubuntu.

- Recherche un paquet dans vos sources actuelles :

`apt-cache search {{query}}`

- Affiche des informations sur un paquet :

`apt-cache show {{package}}`

- Indique si un paquet est installé et à jour :

`apt-cache policy {{package}}`

- Affiche les dépendances d'un paquet :

`apt-cache depends {{package}}`

- Affiche les paquets qui dépendent d'un paquet particulier :

`apt-cache rdepends {{package}}`
