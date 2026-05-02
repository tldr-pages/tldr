# litestream

> Continuous replication and disaster recovery tool for SQLite databases.
> More information: <https://litestream.io>.

- Replicate a database to an S3 bucket:

`litestream replicate {{path/to/db.sqlite}} s3://{{bucket-name}}/{{db.sqlite}}`

- Restore a database from a replica:

`litestream restore -o {{path/to/db.sqlite}} s3://{{bucket-name}}/{{db.sqlite}}`

- Replicate using a configuration file:

`litestream replicate -config {{path/to/litestream.yml}}`

- List all databases and their replicas from a config file:

`litestream databases -config {{path/to/litestream.yml}}`

- Replicate to a local directory:

`litestream replicate {{path/to/db.sqlite}} file://{{path/to/replica/dir}}`
