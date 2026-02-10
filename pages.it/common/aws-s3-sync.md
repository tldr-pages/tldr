# aws s3 sync

> Sincronizza ricorsivamente file e directory tra il tuo sistema locale e un bucket S3, o tra bucket S3.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html>.

- Sincronizza i file in una directory da locale a un bucket:

`aws s3 sync {{percorso/della/directory}} s3://{{nome_bucket}}/{{percorso/della/remote_location}}`

- Sincronizza i file in una directory da un bucket a locale:

`aws s3 sync s3://{{nome_bucket}}/{{percorso/della/remote_location}} {{percorso/della/directory}}`

- Sincronizza oggetti tra due bucket:

`aws s3 sync s3://{{bucket_source_name}}/{{percorso/della/remote_location}} s3://{{bucket_target_name}}/{{percorso/della/remote_location}}`

- Sincronizza file locali su S3 escludendo file o directory specifici:

`aws s3 sync {{percorso/della/directory}} s3://{{nome_bucket}}/{{percorso/della/remote_location}} --exclude {{percorso/del/file}} --exclude {{percorso/della/directory}}/*`

- Sincronizza oggetti tra bucket ed elimina i file di destinazione non presenti nella sorgente:

`aws s3 sync s3://{{bucket_source_name}}/{{percorso/della/remote_location}} s3://{{bucket_target_name}}/{{percorso/della/remote_location}} --delete`

- Sincronizza su S3 con opzioni avanzate (imposta ACL e classe di storage):

`aws s3 sync {{percorso/della/local_directory}} s3://{{nome_bucket}}/{{percorso/della/remote_location}} --acl {{private|public-read}} --storage-class {{STANDARD_IA|GLACIER}}`

- Sincronizza file su S3 e salta quelli non modificati (confronta dimensione e tempo di modifica):

`aws s3 sync {{percorso/della/directory}} s3://{{nome_bucket}}/{{percorso/della/remote_location}} --size-only`

- Visualizza l'aiuto:

`aws s3 sync help`
