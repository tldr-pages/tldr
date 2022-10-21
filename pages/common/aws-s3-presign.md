# aws s3 presign

> Generate a pre-signed URL for an Amazon S3 object.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- Generate a pre-signed URL for a specific bucket and key that is valid for one hour:

`aws s3 presign s3://{{example_bucket_name}}/{{file_name}}.txt`

- Generate a pre-signed URL with a custom lifetime:

`aws s3 presign s3://{{example_bucket_name}}/{{file_name}}.txt --expires-in {{604800}}`

- Display help:

`aws s3 presign help`
