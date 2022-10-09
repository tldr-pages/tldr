# aws s3 ls

> List AWS S3 buckets, folders (prefixes), and files (objects).
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- List all buckets:

`aws s3 ls`

- List files and folders in the root of a bucket (`s3://` is optional):

`aws s3 ls s3://{{bucket_name}}`

- List files and folders directly inside a directory:

`aws s3 ls {{bucket_name}}/{{path/to/directory}}/`

- List all files in a bucket:

`aws s3 ls --recursive {{bucket_name}}`

- List all files in a path with a given prefix:

`aws s3 ls --recursive {{bucket_name}}/{{path/to/directory/}}{{prefix}}`

- Display help:

`aws s3 ls help`
