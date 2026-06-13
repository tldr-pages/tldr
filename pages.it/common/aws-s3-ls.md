# aws s3 ls

> Elenca bucket AWS S3, cartelle (prefissi) e file (oggetti).
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html>.

- Elenca tutti i bucket:

`aws s3 ls`

- Elenca file e cartelle nella radice di un bucket (`s3://` è opzionale):

`aws s3 ls s3://{{nome_bucket}}`

- Elenca file e cartelle direttamente all'interno di una directory:

`aws s3 ls {{nome_bucket}}/{{percorso/della/directory}}/`

- Elenca tutti i file in un bucket:

`aws s3 ls --recursive {{nome_bucket}}`

- Elenca tutti i file in un percorso con un prefisso dato:

`aws s3 ls --recursive {{nome_bucket}}/{{percorso/della/directory}}/{{prefisso}}`

- Visualizza l'aiuto:

`aws s3 ls help`
