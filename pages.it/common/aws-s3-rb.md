# aws s3 rb

> Elimina un bucket S3 vuoto.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- Elimina un bucket S3 vuoto:

`aws s3 rb s3://{{nome_bucket}}`

- Forza l'eliminazione di un bucket S3 e dei suoi oggetti non versionati (fallirà se sono presenti oggetti versionati):

`aws s3 rb s3://{{nome_bucket}} --force`
