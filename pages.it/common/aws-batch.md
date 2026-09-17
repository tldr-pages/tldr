# aws batch

> Esegue carichi di lavoro di calcolo batch tramite il servizio AWS Batch.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/batch/>.

- Elenca i lavori batch in esecuzione:

`aws batch list-jobs --job-queue {{nome_coda}}`

- Crea ambiente di calcolo:

`aws batch create-compute-environment --compute-environment-name {{nome_compute_environment}} --type {{tipo}}`

- Crea coda di lavori batch:

`aws batch create-job-queue --job-queue-name {{nome_coda}} --priority {{priorita'}} --compute-environment-order {{compute_environment}}`

- Invia lavoro:

`aws batch submit-job --job-name {{nome_job}} --job-queue {{coda_job}} --job-definition {{definizione_job}}`

- Descrivi l'elenco dei lavori batch:

`aws batch describe-jobs --jobs {{jobs}}`

- Annulla lavoro:

`aws batch cancel-job --job-id {{id_job}} --reason {{motivazione}}`
