# aws rds

> CLI for AWS Relational Database Service. Relációs adatbázisok létrehozása és kezelése. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Súgó megjelenítése az adott RDS alparancshoz:

`aws rds {{subcommand}} help`

- Stop instance (Példa leállítása):

`aws rds stop-db-instance --db-instance-identifier {{instance_identifier}}`

- Példa indítása:

`aws rds start-db-instance --db-instance-identifier {{instance_identifier}}`

- RDS-példány módosítása:

`aws rds modify-db-instance --db-instance-identifier {{instance_identifier}} {{parameters}} --apply-immediately`

- Frissítések alkalmazása egy RDS-példányra:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- Egy példány azonosítójának módosítása:

`aws rds modify-db-instance --db-instance-identifier {{old_instance_identifier}} --new-db-instance-identifier {{new_instance_identifier}}`

- Egy példány újraindítása:

`aws rds reboot-db-instance --db-instance-identifier {{instance_identifier}}`

- Példa törlése:

`aws rds delete-db-instance --db-instance-identifier {{instance_identifier}} --final-db-snapshot-identifier {{snapshot_identifier}} --delete-automated-backups`
