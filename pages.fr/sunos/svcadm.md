# svcadm

> Manipule les instances de service.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1m/svcadm>.

- Active un service dans la base de données de service :

`svcadm enable {{nom_du_service}}`

- Désactive le service :

`svcadm disable {{nom_du_service}}`

- Redémarre un service en cours d'exécution :

`svcadm restart {{nom_du_service}}`

- Relit les fichiers de configuration :

`svcadm refresh {{nom_du_service}}`

- Efface un service de l'état de maintenance et lui ordonne de démarrer :

`svcadm clear {{nom_du_service}}`
