# vagrant upload

> Upload files and directories from the host to the guest machine.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/upload>.

- Upload file or directory from the host to the guest machine:

`vagrant upload {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Compress the file or directory before uploading to guest machine:

`vagrant upload --compress {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Specify which type of compression to use. Default type is `zip`:

`vagrant upload --compression-type {{tgz|zip}} {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Create a temporary location on the guest machine and upload files to that location:

`vagrant upload --temporary {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`
