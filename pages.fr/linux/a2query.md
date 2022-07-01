# a2query

> Retourne la configuration d'exécution d'Apache sur une distribution Debian.
> Plus d'informations : <https://manpages.debian.org/latest/apache2/a2query.html>.

- Liste les [m]odules Apache actifs :

`sudo a2query -m`

- Vérifie si un module spécifique est installé :

`sudo a2query -m {{nom_module}}`

- Liste les hôtes virtuels actifs :

`sudo a2query -s`

- Affiche le [M]odule de traitement multiple actif :

`sudo a2query -M`

- Affiche la [v]ersion d'Apache :

`sudo a2query -v`
