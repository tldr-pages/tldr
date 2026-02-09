# aws s3 cp

> Copia file locali o oggetti S3 in un'altra posizione localmente o in S3.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html>.

- Copia un file da locale a un bucket specifico:

`aws s3 cp {{percorso/del/file}} s3://{{nome_bucket}}/{{percorso/del/remote_file}}`

- Copia un oggetto S3 specifico in un altro bucket:

`aws s3 cp s3://{{nome_bucket1}}/{{percorso/del/file}} s3://{{nome_bucket2}}/{{percorso/del/target}}`

- Copia un oggetto S3 specifico in un altro bucket mantenendo il nome originale:

`aws s3 cp s3://{{nome_bucket1}}/{{percorso/del/file}} s3://{{nome_bucket2}}`

- Copia oggetti S3 in una directory locale ricorsivamente:

`aws s3 cp s3://{{nome_bucket}} . --recursive`

- Visualizza l'aiuto:

`aws s3 cp help`
