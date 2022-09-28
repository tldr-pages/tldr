# docker logs

> Affiche les journaux d'un conteneur.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/logs>.

- Afficher les journaux d'un conteneur :

`docker logs {{nom_du_conteneur}}`

- Afficher les journaux d'un conteneur en les suivants :

`docker logs -f {{nom_du_conteneur}}`

- Afficher les 5 dernière lignes des journaux d'un conteneur :

`docker logs {{nom_du_conteneur}} --tail {{5}}`

- Afficher les journaux d'un conteneur avec l'horodatage :

`docker logs -t {{nom_du_conteneur}}`

- Afficher les journaux d'un conteneur depuis un certain temps (i.e. 23m, 10s, 2013-01-02T13:23:37) :

`docker logs {{nom_du_conteneur}} --until {{temps}}`
