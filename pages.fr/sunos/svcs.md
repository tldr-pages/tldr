# svcs

> Répertorier les informations sur les services en cours d'exécution.
> Plus d'information : <https://www.unix.com/man-page/linux/1/svcs>.

- Lister tous les services en cours d'exécution :

`svcs`

- Lister les services qui ne fonctionnent pas :

`svcs -vx`

- Répertorier les informations sur un service :

`svcs apache`

- Afficher l'emplacement du fichier journal de service :

`svcs -L apache`

- Afficher la fin d'un fichier journal de service :

`tail $(svcs -L apache)`
