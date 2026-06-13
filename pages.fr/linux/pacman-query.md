# pacman --query

> Fais des requêtes dans la base de données des paquets installés.
> Voir aussi : `pacman`.
> Plus d'informations : <https://manned.org/pacman.8>.

- Liste les paquets installés et leur version :

`pacman -Q`

- Liste uniquement les paquets installés explicitement :

`pacman -Qe`

- Trouve le paquet propriétaire d'un fichier :

`pacman -Qo {{fichier}}`

- Affiche des informations sur un paquet installé :

`pacman -Qi {{paquet}}`

- Liste les fichiers appartenant à un paquet :

`pacman -Ql {{paquet}}`

- Liste les paquets orphelins (installés en tant que dépendances mais requis par aucun paquet installé) :

`pacman -Qdtq`

- Liste les paquets installés ne se trouvant pas dans les dépôts :

`pacman -Qm`

- Liste les paquets périmés :

`pacman -Qu`
