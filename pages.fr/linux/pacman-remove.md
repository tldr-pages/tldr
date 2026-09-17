# pacman --remove

> Supprimes des paquets.
> Voir aussi : `pacman`.
> Plus d'informations : <https://manned.org/pacman.8>.

- Supprime un paquet et ses dépendances :

`sudo pacman -Rs {{paquet}}`

- Supprime un paquet, ses dépendances et ses fichiers de configuration :

`sudo pacman -Rsn {{paquet}}`

- Supprime un paquet silencieusement :

`sudo pacman -R --noconfirm {{paquet}}`

- Supprime les paquets orphelins (installés en tant que dépendance mais requis par aucun paquet installé) :

`sudo pacman -Rsn $(pacman -Qdtq)`

- Supprime un paquet et les paquets qui en dépendent :

`sudo pacman -Rc {{paquet}}`

- Affiche les paquets qui seraient affectés par la commande sans agir :

`pacman -Rp {{paquet}}`

- Affiche l'aide :

`pacman -Rh`
