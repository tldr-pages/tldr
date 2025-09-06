# aws s3 rb

> Delete an empty S3 bucket.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- Delete an empty S3 bucket:

`aws s3 rb s3://{{bucket_name}}`

- Force delete an S3 bucket and its non-versioned objects (will crash if versioned objects are present):

`aws s3 rb s3://{{bucket_name}} --force`
