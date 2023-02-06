# aws s3 presign

> Előre aláírt URL-címek generálása az Amazon S3 objektumokhoz. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- Előre aláírt URL generálása egy adott S3 objektumhoz, amely egy órán keresztül érvényes:

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}}`

- Előre aláírt URL generálása, amely egy adott élettartamra érvényes:

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}} --expires-in {{duration_in_seconds}}`

- Súgó megjelenítése:

`aws s3 presign help`
