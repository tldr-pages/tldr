# b2-tools

> Access all features of Backblaze B2 Cloud Storage easily.
> More information: <https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- Access your account:

`b2 authorize_account {{key_id}}`

- List the existing buckets in your account:

`b2 list_buckets`

- Create a bucket, provide the bucket name, and access type (e.g. allPublic or allPrivate):

`b2 create_bucket {{bucket_name}} {{allPublic|allPrivate}}`

- Upload a file. Choose a file, bucket, and a folder:

`b2 upload_file {{bucket_name}} {{path/to/file}} {{folder_name}}`

- Upload a source directory to a Backblaze B2 bucket destination:

`b2 sync {{path/to/source_file}} {{bucket_name}}`

- Copy a file from one bucket to another bucket:

`b2 copy-file-by-id {{path/to/source_file_id}} {{destination_bucket_name}} {{path/to/b2_file}}`

- Show the files in your bucket:

`b2 ls {{bucket_name}}`

- Remove a "folder" or a set of files matching a pattern:

`b2 rm {{path/to/folder|pattern}}`
