# s3cmd

> Command line tool and client for uploading, retrieveing and managing data in S3 compatible object storage.
> More information: <https://s3tools.org/s3cmd>.

- Initial configuration:

`s3cmd --configure`

- List Buckets/Folders/Objects:

`s3cmd ls s3://{{bucket}}`

- Make Bucket/Folder:

`s3cmd mb s3://{{bucket}}`

- Get file from Bucket:

`s3cmd get s3://{{bucket}}/{{file}} {{local_file}}`

- Put file into bucket:

`s3cmd put {{local_file}} s3://{{bucket}}/{{file}}`

- Move an object to a specific bucket location:

`s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}`

- Delete a specific object:

`s3cmd rm s3://{{bucket}}/{{object}}`
