# svcadm

> Manipuler les instances de service.
> Plus d'information : <https://www.unix.com/man-page/linux/1m/svcadm>.

- Activer un service dans la base de données de service:

`svcadm enable {{nom_du_service}}`

- Désactiver le service:

`svcadm disable {{nom_du_service}}`

- Redémarrer un service en cours d'exécution:

`svcadm restart {{nom_du_service}}`

- Service de commande pour relire les fichiers de configuration:

`svcadm refresh {{nom_du_service}}`

- Effacer un service de l'état de maintenance et lui ordonner de démarrer:

`svcadm clear {{nom_du_service}}`
