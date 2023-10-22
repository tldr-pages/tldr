# aws rds

> CLI para AWS Relational Database Service.
> Crea y administra bases de datos relacionales.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Muestra ayuda para subcomando RDS específicos:

`aws rds {{subcommand}} help`

- Detiene instancia:

`aws rds stop-db-instance --db-instance-identifier {{identificador_de_instancia}}`

- Inicia instancia:

`aws rds start-db-instance --db-instance-identifier {{identificador_de_instancia}}`

- Modifica una instancia RDS:

`aws rds modify-db-instance --db-instance-identifier {{identificador_de_instancia}} {{parametros}} --apply-immediately`

- Aplica actualizaciones a una instancia RDS:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- Modifica un identificador de instancia:

`aws rds modify-db-instance --db-instance-identifier {{antiguo_identificador_instancia}} --new-db-instance-identifier {{nuevo_identificador_instance}}`

- Reinicia una instancia:

`aws rds reboot-db-instance --db-instance-identifier {{identificador_de_instancia}}`

- Eliminar una instancia:

`aws rds delete-db-instance --db-instance-identifier {{identificador_de_instancia}} --final-db-snapshot-identifier {{identificador_snapshot}} --delete-automated-backups`
