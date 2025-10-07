# pacrepairdb

> Fix corrupted database entries in libalpm database.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairdb.pod>.

- Perform a basic repair on a specific package:

`pacrepairdb {{package_name}}`

- Update the database entries without extracting or removing any packages:

`pacrepairdb {{package_name}} --dbonly`

- Display the packages to be repaired and the cache packages to be used without making any changes:

`pacrepairdb {{package_name}} --print-only`

- Display additional progress and debug information:

`pacrepairdb {{package_name}} --verbose`

- Display help:

`pacrepairdb --help`

- Display version:

`pacrepairdb --version`
