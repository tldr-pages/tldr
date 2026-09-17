# aws s3 mv

> Sposta file locali o oggetti S3 in un'altra posizione localmente o in S3.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html>.

- Sposta un file da locale a un bucket specificato:

`aws s3 mv {{percorso/del/local_file}} s3://{{nome_bucket}}/{{percorso/del/remote_file}}`

- Sposta un oggetto S3 specifico in un altro bucket:

`aws s3 mv s3://{{nome_bucket}}/{{percorso/del/file}} s3://{{nome_bucket2}}/{{percorso/del/target}}`

- Sposta un oggetto S3 specifico in un altro bucket mantenendo il nome originale:

`aws s3 mv s3://{{nome_bucket}}/{{percorso/del/file}} s3://{{nome_bucket2}}`

- Visualizza l'aiuto:

`aws s3 mv help`
