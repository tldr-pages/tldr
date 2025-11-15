# kopia

> Fast, secure open-source backup tool.
> Supports encryption, compression, deduplication, and incremental snapshots.
> More information: <https://kopia.io/docs/reference/command-line/>.

- Create a repository in the local filesystem:

`kopia repository create filesystem --path {{path/to/local_repository}}`

- Create a repository on Amazon S3:

`kopia repository create s3 --bucket {{bucket_name}} --access-key {{AWS_access_key_id}} --secret-access-key {{AWS_secret_access_key}}`

- Connect to a repository:

`kopia repository connect {{repository_type}} --path {{path/to/repository}}`

- Create a snapshot of a directory:

`kopia snapshot create {{path/to/directory}}`

- List snapshots:

`kopia snapshot list`

- Restore a snapshot to a specific directory:

`kopia snapshot restore {{snapshot_id}} {{path/to/target_directory}}`

- Create a new policy:

`kopia policy set --global --keep-latest {{number_of_snapshots_to_keep}} --compression {{compression_algorithm}}`

- Ignore a specific file or folder from backups:

`kopia policy set --global --add-ignore {{path/to/file_or_folder}}`
