# apt-mark

> Utilitaire permettant de modifier l'état des paquets installés.
> Plus d'informations : <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Marquer un paquet comme étant automatiquement installé :

`sudo apt-mark auto {{package_name}}`

- Maintenir un paquet à sa version actuelle et empêcher les mises à jour :

`sudo apt-mark hold {{package_name}}`

- Permettre une nouvelle mise à jour d'un paquet :

`sudo apt-mark unhold {{package_name}}`

- Afficher les paquets installés manuellement :

`apt-mark showmanual`

- Afficher les paquets détenus qui ne sont pas mis à jour :

`apt-mark showhold`
