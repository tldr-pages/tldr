# aws logs

> Interagisce con i file di log di vari servizi AWS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/logs/>.

- Elenca i gruppi di log:

`aws logs list-log-groups`

- Interroga continuamente i log di un gruppo CloudWatch:

`aws logs tail {{nome_gruppo_log}} --follow`

- Mostra i log di un gruppo CloudWatch in base a un filtro:

`aws logs tail {{nome_gruppo_log}} --filter-pattern {{pattern}}`

- Trasmette quasi in tempo reale i log di un gruppo:

`aws logs start-live-tail --log-group-identifiers {{nome_gruppo_log}}`

- Esporta i log in un bucket S3:

`aws logs create-export-task --log-group-name {{nome_gruppo_log}} --from {{ora_inizio}} --to {{ora_fine}} --destination {{nome_bucket_s3}}`
