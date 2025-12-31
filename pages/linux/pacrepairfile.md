# pacrepairfile

> Reset properties on files managed by alpm.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairfile.pod>.

- Search for the package and reset the properties of a file:

`pacrepairfile {{path/to/file}} --package`

- Reset a file quietly:

`pacrepairfile {{package_name}} --quiet --package`

- Reset specific file properties (mode, owner UID, group GID, or modification time):

`pacrepairfile {{package_name}} --{{mode|gid|mtime|uid}} --package`

- Display help:

`pacrepairfile --help`

- Display version:

`pacrepairfile --version`
