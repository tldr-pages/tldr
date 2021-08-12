# aws s3

> CLI pentru AWS S3 - oferă stocare prin interfețe de servicii web.
> Mai multe informaţii: <https://aws.amazon.com/cli>

- Afișează fișierele într-o găleată:

`aws s3 ls {{bucket_name}}`

- Sincronizarea fișierelor și directoarelor de la local la găleată:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}}`

- Sincronizarea fișierelor și directoarelor de la găleată la locală:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- Sincronizarea fișierelor și directoarelor cu excluderi:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Elimină fișierul din găleată:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Examinaţi doar modificările:

`aws s3 {{any_command}} --dryrun`
