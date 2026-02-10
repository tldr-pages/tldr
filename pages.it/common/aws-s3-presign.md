# aws s3 presign

> Genera URL pre-firmati per oggetti Amazon S3.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html>.

- Genera un URL pre-firmato per un oggetto S3 specifico valido per un'ora:

`aws s3 presign s3://{{nome_bucket}}/{{percorso/del/file}}`

- Genera un URL pre-firmato valido per una durata specifica:

`aws s3 presign s3://{{nome_bucket}}/{{percorso/del/file}} --expires-in {{durata_in_secondi}}`

- Visualizza l'aiuto:

`aws s3 presign help`
