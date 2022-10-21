# aws s3 mb

> Create an S3 bucket.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mb.html>.

- Create an S3 bucket:

`aws s3 cp {{file_name}} s3://{{example_bucket_name}}/{{file_name}}.txt`

- Create an S3 bucket in a specific region:

`aws s3 mb s3://{{example_bucket_name}} --region {{region_value}}`

- Display help:

`aws s3 mb help`
