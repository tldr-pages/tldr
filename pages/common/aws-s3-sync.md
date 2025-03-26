# aws s3 sync

> Recursively sync files and directories between your local system and an S3 bucket, or between S3 buckets.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html>.

- Sync files and directories from local to a bucket:

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- Sync files and directories from a bucket to local:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} {{path/to/file_or_directory}}`

- Sync objects between two buckets:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- Sync local files to S3 while excluding specific files or directories:

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Sync objects between buckets and delete destination files not in source:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --delete`

- Sync to S3 with advanced options (set ACL and storage class):

`aws s3 sync {{path/to/local_directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --acl {{private|public-read}} --storage-class {{STANDARD_IA|GLACIER}}`

- Sync files to S3 and skip unchanged ones (compare size and modification time):

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --size-only`

- Display help:

`aws s3 sync help`
