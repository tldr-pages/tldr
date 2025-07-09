# mc

> MinIO Client for object storage and filesystems.
> May be named `mc` or `mcli` on some systems.
> More information: <https://minio.github.io/mc/>.

- Add connection to a S3 server:

`mc alias set {{local}} {{http://localhost:9000}} {{access_key}} {{secret_key}}`

- Create a bucket:

`mc mb {{local/bucket_name}}`

- List buckets and their content recursively:

`mc ls {{local}} --recursive`
