# aws s3 rm

> Delete an S3 object.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- Delete a single S3 object:

`aws s3 rm s3://{{example_bucket_name}}/{{file_name}}.txt`

- Perform a dry-run of a single S3 object deletion:

`aws s3 rm s3://{{example_bucket_name}}/{{file_name}}.txt --dryrun`

- Delete an object from an S3 access point:

`aws s3 rm s3://arn:aws:s3:us-west-2:123456789012:{{access_point}}/{{my_access_point}}/{{my_key}}`

- Display help:

`aws s3 rm help`
