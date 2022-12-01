# mkisofs

> Create ISO files from directories.
> Also aliased as `genisoimage`.
> More information: <https://manned.org/mkisofs>.

- Create an ISO from a directory:

`mkisofs -o {{path/to/file.iso}} {{path/to/source_directory}}`

- Set the disc label when creating an ISO:

`mkisofs -o {{path/to/file.iso}} -V "{{label_name}}" {{path/to/source_directory}}`
