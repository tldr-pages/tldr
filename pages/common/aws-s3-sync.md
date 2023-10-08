# aws s3 sync

> Sync files and directories between local and a S3 bucket or S3 objects between S3 buckets recursively
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html>.

- Sync files and directories from local to a specific bucket location:

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- Sync files and directories from specific bucket location to local:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} {{path/to/file_or_directory}}`

- Sync S3 objects between buckets:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_object_or_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- Sync files and directories from local to S3 bucket excluding some files or directory:

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Sync objects between buckets deleting all objects that not exist in the source location. Use this command with caution because objects will be removed in the target bucket:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_object_or_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --delete`

- Display help:

`aws s3 sync help`
