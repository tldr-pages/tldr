# b2-tools

> Command-line tool that gives easy access to all of the capabilities of Backblaze B2 Cloud Storage.
> More information: <https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- Tell the command-line tool how to access your account:

`b2 authorize_account {{keyid}}`

- List the existing buckets in your account:

`b2 list_buckets`

- Create a bucket, provide the bucket name, and access type (e.g. allPublic) or (e.g. allPrivate):

`b2 create_bucket {{bucket_name}} {{allPublic|allPrivate}}`

- Upload a file, choose a file, bucket and a folder:

`b2 upload_file {{bucket_name}} {{file_name}} {{folder_name}}`

- Upload a source directory to a Backblaze B2 bucket destination:

`b2 sync {{source_file_location}} {{bucket_name}}`

- Copy a file from one bucket to another bucket:

`b2 copy-file-by-id {{source_file_id}} {{destination_bucket_name}} {{b2_file_name}}`

- Show the files in your bucket:

`b2 ls {{bucket_name}}`

- Remove a "folder" or a set of files matching a pattern:

`b2 rm {{folder_name}}`
