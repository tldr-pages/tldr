# minio server

> MinIO server command for starting the MinIO S3 compatible storage engine.
> More information: <https://github.com/minio/minio>.

- Start a server using the default configuration:

`minio server {{path/to/data_directory}}`

- Start a server binding to a different port for the API and web console:

`minio server --address ":42069" --console-address ":8008" {{path/to/data_directory}}`

- Start a server as part of a cluster of 2 nodes:

`minio server {{node1_hostname}} {{path/to/data_directory}} {{node2_hostname}} {{path/to/data_directory}}`
