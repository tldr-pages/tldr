# aws s3 rm

> Delete S3 objects.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- Delete a specific S3 object:

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}}`

- Perform a dry-run of a single S3 object deletion:

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}} --dryrun`

- Delete an object from a specific S3 access point:

`aws s3 rm s3://arn:aws:s3:us-west-2:123456789012:{{access_point}}/{{my_access_point}}/{{my_key}}`

- Display help:

`aws s3 rm help`
