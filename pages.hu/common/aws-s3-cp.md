# aws s3 cp

> Helyi fájlok vagy S3 objektumok másolása egy másik helyre helyben vagy az S3-ban. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

- Fájl másolása helyi fájlból egy adott vödörbe:

`aws s3 cp {{path/to/file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- Egy adott S3 objektum másolása egy másik vödörbe:

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- Egy adott S3 objektum másolása egy másik vödörbe az eredeti nevet megtartva:

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- S3 objektumok másolása egy helyi könyvtárba rekurzívan:

`aws s3 cp s3://{{bucket_name}} . --recursive`

- Súgó megjelenítése:

`aws s3 cp help`
