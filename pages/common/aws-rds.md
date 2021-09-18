# aws rds

> CLI for AWS RDS.
> Create and manage relational databases.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Show help for specific RDS subcommand:

`aws rds {{subcommand}} help`

- Stop instance:

`aws rds stop-db-instance --db-instance-identifier {{instance_identifier}}`

- Start instance:

`aws rds start-db-instance --db-instance-identifier {{instance_identifier}}`

- Modify an RDS instance:

`aws rds modify-db-instance --db-instance-identifier {{instance_identifier}} {{parameters}} --apply-immediately`

- Apply updates to RDS instance:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action system-update --opt-in-type immediate`

- Change instance identifier:

`aws rds modify-db-instance --db-instance-identifier {{old_instance_identifier}}  --new-db-instance-identifier {{new_instance_identifier}}`

- Reboot instance:

`aws rds reboot-db-instance --db-instance-identifier {{instance_identifier}}`

- Delete instance:

`aws rds delete-db-instance --db-instance-identifier {{instance_identifier}} --final-db-snapshot-identifier {{finalsnapshot}} --delete-automated-backups`
