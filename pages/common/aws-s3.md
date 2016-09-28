# aws s3

> CLI for AWS S3 - provides storage through web services interfaces.

- Sync files and folders from local to bucket:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}}`

- Sync files and folders from bucket to local:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- Sync files and folders with exclusions:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/folder}}/*`

- Copy from one bucket to another recursively:

`aws s3 cp s3://{{source_bucket}}/{{path/to/file}} s3://{{destination_bucket}} --recursive`

- Remove file from bucket:

`aws s3 rm s3://{{source_bucket}}/{{path/to/file}}`

- Preview changes only:

`aws s3 {{any_command}} --dryrun`
