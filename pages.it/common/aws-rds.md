# aws rds

> Utilizza AWS Relational Database Service, un servizio web per impostare, operare e scalare database relazionali.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/rds/>.

- Visualizza l'aiuto per un sottocomando RDS specifico:

`aws rds {{subcommand}} help`

- Ferma l'istanza:

`aws rds stop-db-instance --db-instance-identifier {{identificativo_istanza}}`

- Avvia l'istanza:

`aws rds start-db-instance --db-instance-identifier {{identificativo_istanza}}`

- Modifica un'istanza RDS:

`aws rds modify-db-instance --db-instance-identifier {{identificativo_istanza}} {{parametri}} --apply-immediately`

- Applica aggiornamenti a un'istanza RDS:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- Cambia l'identificativo dell'istanza:

`aws rds modify-db-instance --db-instance-identifier {{old_identificativo_istanza}} --new-db-instance-identifier {{nuovo_identificativo_istanza}}`

- Riavvia l'istanza:

`aws rds reboot-db-instance --db-instance-identifier {{identificativo_istanza}}`

- Elimina l'istanza:

`aws rds delete-db-instance --db-instance-identifier {{identificativo_istanza}} --final-db-snapshot-identifier {{identificativo_snapshot}} --delete-automated-backups`
