# aws s3

> CLI az AWS S3-hoz - tárhelyet biztosít webes szolgáltatási interfészeken keresztül. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Fájlok megjelenítése egy vödörben:

`aws s3 ls {{bucket_name}}`

- Fájlok és könyvtárak szinkronizálása a lokálisból a vödörbe:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}}`

- Fájlok és könyvtárak szinkronizálása a vödörből a lokálisba:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- Fájlok és könyvtárak szinkronizálása kizárásokkal:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Fájl eltávolítása a vödörből:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Csak a változások előnézete:

`aws s3 {{any_command}} --dryrun`
