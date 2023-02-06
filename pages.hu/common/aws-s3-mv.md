# aws s3 mv

> Helyi fájlok vagy S3 objektumok áthelyezése egy másik helyre helyben vagy az S3-ban. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- Fájl áthelyezése a helyi fájlból egy megadott vödörbe:

`aws s3 mv {{path/to/local_file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- Egy adott S3 objektum áthelyezése egy másik vödörbe:

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- Egy adott S3 objektum áthelyezése egy másik vödörbe az eredeti nevet megtartva:

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- Súgó megjelenítése:

`aws s3 mv help`
