# pacrepairfile

> Reset properties on files managed by alpm.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairfile.pod>.

- Search for the package that owns a given file:

`pacrepairfile {{file_path}} --package`

- Reset a File Quietly:

`pacrepairfile {{package_name}} --quiet --package`

- Reset specific file properties (mode, owner UID, group GID, or modification time):

`pacrepairfile {{package_name}} --{{mode|gid|mtime|uid}} --package`

- Display help:

`pacrepairfile --help`

- Display version:

`pacrepairfile --version`
