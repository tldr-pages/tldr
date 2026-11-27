# apt-mark

> Utilitaire permettant de modifier l'état des paquets installés.
> Plus d'informations : <https://manned.org/apt-mark>.

- Marque un paquet comme étant automatiquement installé :

`sudo apt-mark auto {{paquet}}`

- Maintient un paquet à sa version actuelle et empêche les mises à jour :

`sudo apt-mark hold {{paquet}}`

- Permet une nouvelle mise à jour d'un paquet :

`sudo apt-mark unhold {{paquet}}`

- Affiche les paquets installés manuellement :

`apt-mark showmanual`

- Affiche les paquets détenus qui ne sont pas mis à jour :

`apt-mark showhold`
