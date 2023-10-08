# aws s3

> CLI for AWS S3 - provides storage through web services interfaces.
> Some subcommands such as `cp`, `ls`, `mb`, `mv`, `sync`, etc. have their own usage documentation.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Show files in a bucket:

`aws s3 ls {{bucket_name}}`

- Remove file from bucket:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Preview changes only:

`aws s3 {{any_command}} --dryrun`
