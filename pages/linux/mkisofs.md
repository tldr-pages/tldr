# mkisofs

> Create ISO files from directories.
> Also aliased as `genisoimage`.

- Create an ISO from a directory:

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- Set the disc label when creating an ISO:

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`
