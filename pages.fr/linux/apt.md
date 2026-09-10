# apt

> Utilitaire de gestion des paquets pour les distributions basées sur Debian.
> Conçue comme une alternative conviviale à `apt-get` pour une utilisation interactive.
> Pour les commandes équivalentes dans d’autres gestionnaires de paquets, voir <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Plus d'informations : <https://manned.org/apt.8>.

- Met à jour la liste des paquets et des versions disponibles (il est recommandé de l'exécuter avant les autres commandes `apt`) :

`sudo apt update`

- Recherche d'un paquet donné :

`apt search {{package}}`

- Recherche des paquets uniquement par nom (accepte les caractères joker comme `*`) :

`apt list {{package}}`

- Affiche les informations pour un paquet :

`apt show {{package}}`

- Installe un paquet, ou le met à jour avec la dernière version disponible :

`sudo apt install {{package}}`

- Supprime un paquet (utiliser `purge` à la place supprime également ses fichiers de configuration) :

`sudo apt remove {{package}}`

- Met à jour tous les paquets installés vers les dernières versions disponibles :

`sudo apt upgrade`

- Liste les paquets installés :

`apt list {{[-i|--installed]}}`
