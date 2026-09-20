# svcs

> Répertorier les informations sur les services en cours d'exécution.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1/svcs>.

- Liste tous les services en cours d'exécution :

`svcs`

- Liste les services qui ne fonctionnent pas :

`svcs -vx`

- Répertorie les informations sur un service :

`svcs apache`

- Affiche l'emplacement du fichier journal de service :

`svcs -L apache`

- Affiche la fin d'un fichier journal de service :

`tail $(svcs -L apache)`
