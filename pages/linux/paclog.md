# paclog

> Filter pacman log entries.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclog.pod>.

- Display the entire pacman log:

`paclog`

- Display pacman-style logged commandline entries:

`paclog --commandline`

- Display when modifications have been made to a package:

`paclog --package {{package_name}}`

- Display package actions of a specific type:

`paclog --action {{install|reinstall|upgrade|downgrade|remove|all}}`

- Display only errors, warnings, and notes:

`paclog --warnings`

- Display the list of installed packages according to the log:

`paclog --pkglist`

- Display help:

`paclog --help`

- Display version:

`paclog --version`
