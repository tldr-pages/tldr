# mkisofs

> Create ISO files from folders.
> Also aliased as `genisoimage`.

- Create an ISO from a folder:

`mkisofs -o {{filename.iso}} {{path/to/source_folder}}`

- Set the disc label when creating an ISO:

`mkisofs -o {{filename.iso}} -V {{"label_name"}} {{path/to/source_folder}}`
