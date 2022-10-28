# svcadm

> Manipuler les instances de service.
> Plus d'information : <https://www.unix.com/man-page/linux/1m/svcadm>.

- Activer un service dans la base de données de service:

`svcadm enable {{service_name}}`

- Désactiver le service:

`svcadm disable {{service_name}}`

- Redémarrer un service en cours d'exécution:

`svcadm restart {{service_name}}`

- Service de commande pour relire les fichiers de configuration:

`svcadm refresh {{service_name}}`

- Effacer un service de l'état de maintenance et lui ordonner de démarrer:

`svcadm clear {{service_name}}`
