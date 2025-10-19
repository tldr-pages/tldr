# minio server

> MinIO server command for starting the MinIO S3 compatible storage engine.
> More information: <https://github.com/minio/minio>.

- Start a server using the default configuration:

`minio server {{/path/to/data/directory}}`

- Start a server binding to a different port for the API and web console:

`minio server --address ":42069" --console-address ":8008" {{/path/to/data/directory}}`

- Start a server as part of a cluster of 2 nodes:

`minio server {{hostname-of-node1}} {{/path/to/data/directory}} {{hostname-of-node2}} {{/path/to/data/directory}}`
