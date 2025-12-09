# aws backup

> Einheitliches Backup-Service zum Schutz der Amazon Web Services und der damit verbundenen Daten.
> Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Gib Backup-Plan-Details für eine bestimmte Backup-Plan-ID aus:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Erstelle einen Backup-Plan unter Verwendung eines bestimmten Backup-Plan-Namens und von Backup-Regeln:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Lösche einen bestimmten Backup-Plan:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Gib eine Liste aller aktiven Backup-Pläne für das aktuelle Konto aus:

`aws backup list-backup-plans`

- Zeige Details über die Report-Aufträge an:

`aws backup list-report-jobs`
