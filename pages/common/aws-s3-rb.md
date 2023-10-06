# aws s3 rb

> Deletes an empty S3 bucket.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- Deletes an empty S3 bucket:

`aws s3 rb s3://{{bucket_name}}`

- Deletes an S3 bucket and its non versioned objects (will crash if versionned objects):

`aws s3 rb s3://{{bucket_name}} --force`

