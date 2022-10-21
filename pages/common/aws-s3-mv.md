# aws s3 mv

> Move a local file or S3 object to another location locally or in S3.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- Move a single file to a specified bucket and key:

`aws s3 mv {{file_name}} s3://{{example_bucket_name}}/{{file_name_2}}.txt`

- Move a single S3 object to a specified bucket and key:

`aws s3 mv s3://{{example_bucket_name}}/{{file_name}}.txt s3://{{example_bucket_name}}/{{file_name_2}}.txt`

- Move a single S3 object to a specified bucket and retain its original name:

`aws s3 mv s3://{{example_bucket_name}}/{{file_name}}.txt s3://{{example_bucket_name}}`

- Display help:

`aws s3 mv help`
