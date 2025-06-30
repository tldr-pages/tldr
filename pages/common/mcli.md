# mcli

> MinIO Client for object storage and filesystems
> May be named 'mc' on some systems.
> More information: <https://minio.github.io/mc/>.

- Add connection to a S3 server:

`mcli alias set {{local}} {{http://localhost:9000}} {{access_key}} {{secret_key}}`

- Create a bucket:

`mcli mb {{local/bucket_name}}`

- List buckets and their content recursively:

`mcli ls local -r`
