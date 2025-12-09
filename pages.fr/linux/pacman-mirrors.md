# pacman-mirrors

> Génère une liste de miroirs pour pacman sur Manjaro Linux.
> Tout appel à pacman-mirrors demande de synchroniser les bases de données et de mettre à jour le système en exécutant `sudo pacman -Syyu` en suivant.
> Voir aussi: `pacman`.
> Plus d'informations : <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Génère une liste de miroirs avec les réglages par défaut :

`sudo pacman-mirrors --fasttrack`

- Obtiens le statut des miroirs actuels :

`pacman-mirrors --status`

- Affiche la branche courante :

`pacman-mirrors --get-branch`

- Utilise une branche différente :

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Génère une liste de miroirs se trouvant dans le pays associé à l'adresse IP :

`sudo pacman-mirrors --geoip`
