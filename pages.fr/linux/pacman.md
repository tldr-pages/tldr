# pacman

> Outil de gestion de paquets sur Arch Linux. 

- Synchronise et mets à jour tous les paquets:

`pacman -Syu`

- Installe un nouveau paquet:

`pacman -S {{package_name}}`

- Efface un paquet et ses dépendances:

`pacman -Rs {{package_name}}`

- Recherche dans la base de données des paquets une expression régulière ou mot clé:

`pacman -Ss "{{search_pattern}}"`

- Liste les paquets installés et leurs versions:

`pacman -Q`

- Liste seulement les paquets installés explicitement et leurs versions:

`pacman -Qe`

- Trouve à quel paquet un certain fichier appartient:

`pacman -Qo {{filename}}`

- Vide le cache des paquets pour libérer de l'espace:

`pacman -Scc`
