# s3cmd

> Command line tool and client for uploading, retrieveing and managing data in S3 compatible object storage.
> More information: <https://s3tools.org/s3cmd>.

- Invoke configuration/reconfiguration tool:

`s3cmd --configure`

- List Buckets/Folders/Objects:

`s3cmd ls s3://{{bucket|path/to/file}}`

- Create Bucket/Folder:

`s3cmd mb s3://{{bucket}}`

- Download a specific file from a bucket:

`s3cmd get s3://{{bucket_name}}/{{path/to/file}} {{path/to/local_file}}`

- Upload a file to a bucket:

`s3cmd put {{local_file}} s3://{{bucket}}/{{file}}`

- Move an object to a specific bucket location:

`s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}`

- Delete a specific object:

`s3cmd rm s3://{{bucket}}/{{object}}`
