# aws backup

> Einheitliches Backup-Service zum Schutz der Amazon Web Services und der damit verbundenen Daten.
> Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Rückgabe von Backup-Plan-Details für eine bestimmte Backup-Plan-ID:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- Erstellen eines Sicherungsplans unter Verwendung eines bestimmten Sicherungsplannamens und von Sicherungsregeln:

`aws backup create-backup-plan --backup-plan {{plan}}`

- Löschen eines bestimmten Backup-Plans

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- Liefert eine Liste aller aktiven Backup-Pläne für das aktuelle Konto:

`aws backup list-backup-plans`

- Zeigt Deatuls über die Reportaufträge an:

`aws backup list-report-jobs`
