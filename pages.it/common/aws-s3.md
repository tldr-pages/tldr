# aws s3

> CLI per AWS S3 - fornisce spazio di archiviazione tramite le interfacce di Amazon Web Services.
> Maggiori informazioni: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Mostra file in un bucket:

`aws s3 ls {{nome_bucket}}`

- Sincronizza file e directory locali su un bucket:

`aws s3 sync {{percorso/dei/file}} s3://{{nome_bucket}}`

- Sincronizza file e directory da un bucket in locle:

`aws s3 sync s3://{{nome_bucket}} {{percorso/del/file_o_cartella}}`

- Sincronizza file e directory escludendo alcuni file o directory:

`aws s3 sync {{percorso/dei/file}} s3://{{nome_bucket}} --exclude {{percorso/del/file}} --exclude {{directory}}/*`

- Rimuovi un file dal bucket:

`aws s3 rm s3://{{bucket}}/{{percorso/del/file}}`

- Mostra solo un'anteprima dei cambiamenti:

`aws s3 {{qualsiasi_comando}} --dryrun`
