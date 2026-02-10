# aws s3 rm

> Elimina oggetti S3.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html>.

- Elimina un oggetto S3 specifico:

`aws s3 rm s3://{{nome_bucket}}/{{percorso/del/file}}`

- Anteprima l'eliminazione di un oggetto S3 specifico senza eliminarlo (dry-run):

`aws s3 rm s3://{{nome_bucket}}/{{percorso/del/file}} --dryrun`

- Elimina un oggetto da un access point S3 specifico:

`aws s3 rm s3://arn:aws:s3:{{region}}:{{account_id}}:{{access_point}}/{{access_point_name}}/{{object_key}}`

- Rimuove tutti gli oggetti da un bucket (svuota il bucket):

`aws s3 rm s3://{{nome_bucket}} --recursive`

- Visualizza l'aiuto:

`aws s3 rm help`
