# aws backup

> Servizio unificato di backup progettato per proteggere i servizi Amazon Web Services e i relativi dati.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/backup/>.

- Restituisce i dettagli di BackupPlan per un BackupPlanId specifico:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Crea un piano di backup utilizzando un nome di piano di backup specifico e regole di backup:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Elimina un piano di backup specifico:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Elenca tutti i piani di backup attivi per l'account corrente:

`aws backup list-backup-plans`

- Visualizza i dettagli sui lavori di report:

`aws backup list-report-jobs`
