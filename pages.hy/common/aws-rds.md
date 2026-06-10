# aws rds

> Օգտագործեք AWS Relational Database Service, որը վեբ ծառայություն է հարաբերական տվյալների բազաների ստեղծման, շահագործման և մասշտաբավորման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/rds/>:.

- Ցուցադրել օգնություն հատուկ RDS ենթահրամանի համար.:

`aws rds {{subcommand}} help`

- Stop օրինակ.:

`aws rds stop-db-instance --db-instance-identifier {{instance_identifier}}`

- Մեկնարկի օրինակ.:

`aws rds start-db-instance --db-instance-identifier {{instance_identifier}}`

- Փոփոխել RDS օրինակը.:

`aws rds modify-db-instance --db-instance-identifier {{instance_identifier}} {{parameters}} --apply-immediately`

- Կիրառեք թարմացումներ RDS օրինակում.:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- Փոխեք օրինակի նույնացուցիչը.:

`aws rds modify-db-instance --db-instance-identifier {{old_instance_identifier}} --new-db-instance-identifier {{new_instance_identifier}}`

- Վերագործարկեք մի օրինակ.:

`aws rds reboot-db-instance --db-instance-identifier {{instance_identifier}}`

- Ջնջել մի օրինակ.:

`aws rds delete-db-instance --db-instance-identifier {{instance_identifier}} --final-db-snapshot-identifier {{snapshot_identifier}} --delete-automated-backups`
