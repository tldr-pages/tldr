# aws rds

> Nota: Las diferentes implementaciones de AWK suelen convertirlo en un enlace simbólico de su binario.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/rds/>.

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

`aws rds modify-db-instance --db-instance-identifier {{antiguo_identificador_instancia}} --new-db-instance-identifier {{nuevo_identificador_instancia}}`

- Reinicia una instancia:

`aws rds reboot-db-instance --db-instance-identifier {{identificador_de_instancia}}`

- Elimina una instancia:

`aws rds delete-db-instance --db-instance-identifier {{identificador_de_instancia}} --final-db-snapshot-identifier {{identificador_snapshot}} --delete-automated-backups`
