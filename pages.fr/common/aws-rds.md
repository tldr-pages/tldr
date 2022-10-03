# aws rds

> CLI AWS pour Relational Database Service.
> Crée et gère des bases de données relationnelles.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Affiche l'aide pour une sous-commande RDS donnée :

`aws rds {{sous_commande}} help`

- Stoppe une instance :

`aws rds stop-db-instance --db-instance-identifier {{identifiant_de_l_instance}}`

- Démarre une nouvelle instance :

`aws rds start-db-instance --db-instance-identifier {{identifiant_de_l_instance}}`

- Modifie une instance RDS :

`aws rds modify-db-instance --db-instance-identifier {{identifiant_de_l_instance}} {{paramètres}} --apply-immediately`

- Applique les mises à jour à une instance RDS :

`aws rds apply-pending-maintenance-action --resource-identifier {{arn_de_la_base_de_données}} --apply-action {{mise_à_jour_du_système}} --opt-in-type {{immediate}}`

- Change l'identifiant d'une instance :

`aws rds modify-db-instance --db-instance-identifier {{ancien_identifiant_de_l_instance}} --new-db-instance-identifier {{nouvel_identifiant_de_l_instance}}`

- Redémarre une instance :

`aws rds reboot-db-instance --db-instance-identifier {{identifiant_de_l_instance}}`

- Supprime une instance :

`aws rds delete-db-instance --db-instance-identifier {{identifiant_de_l_instance}} --final-db-snapshot-identifier {{identifiant_de_l_image}} --delete-automated-backups`
