# aws s3 rm

> S3 objektumok törlése. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- Egy adott S3 objektum törlése:

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}}`

- Egy adott S3 objektum törlésének előnézete törlés nélkül (szárazfutás):

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}} --dryrun`

- Objektum törlése egy adott S3 hozzáférési pontról:

`aws s3 rm s3://arn:aws:s3:{{region}}:{{account_id}}:{{access_point}}/{{access_point_name}}/{{object_key}}`

- Súgó megjelenítése:

`aws s3 rm help`
