# aws s3

> CLI for AWS S3 - provides storage through web services interfaces.
> Some subcommands such as `cp`, `ls`, `mb`, `mv`, `sync`, etc. have their own usage documentation.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Show files in a bucket:

`aws s3 ls {{bucket_name}}`

- Filter the included or excluded files, directory, objects or extension that will be manipuled in the operations:

`aws s3 {{cp|mv|sync|rm|...}} {{subcommand_options}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/* --include {{*.ext}}`

- Remove file from bucket:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Preview changes only:

`aws s3 {{any_command}} --dryrun`

- Execute the command in a recursive way:

`aws s3 {{cp|mv|rm|...}} --recursive`

- Display help:

`aws s3 help`
