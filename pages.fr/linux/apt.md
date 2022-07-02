# apt

> Utilitaire de gestion des paquets pour les distributions basées sur Debian.
> Remplacement recommandé pour `apt-get` lorsqu'il est utilisé de manière interactive dans les versions 16.04 et ultérieures d'Ubuntu.
> Plus d'informations : <https://manpages.debian.org/latest/apt/apt.8.html>.

- Mettre à jour la liste des paquets et des versions disponibles (il est recommandé de l'exécuter avant les autres commandes `apt`) :

`sudo apt update`

- Recherche d'un paquet donné :

`apt search {{package}}`

- Afficher les informations pour un paquet :

`apt show {{package}}`

- Installer un paquet, ou le mettre à jour avec la dernière version disponible :

`sudo apt install {{package}}`

- Supprimer un paquet (utiliser `purge` à la place supprime également ses fichiers de configuration) :

`sudo apt remove {{package}}`

- Mettre à jour tous les paquets installés vers les dernières versions disponibles :

`sudo apt upgrade`

- Lister tous les paquets :

`apt list`

- Lister les paquets installés :

`apt list --installed`
