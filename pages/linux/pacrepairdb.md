# pacrepairdb

> Fix corrupted database entries in libalpm database.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairdb.pod>.

- Perform a basic repair on a specific package:

`pacrepairdb {{package_name}}`

- Update the database entries without extracting or removing any packages:

`pacrepairdb --dbonly {{package_name}}`

- Display the packages to be repaired and the cache packages to be used without making any changes:

`pacrepairdb --print-only {{package_name}}`

- Display additional progress and debug information:

`pacrepairdb --verbose {{package_name}}`

- Display help:

`pacrepairdb --help`

- Display version:

`pacrepairdb --version`
