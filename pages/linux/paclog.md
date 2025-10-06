# paclog

> Filter pacman log entries.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclog.pod>.

- Display the entire pacman log:

`paclog`

- Display pacman-style logged commandline entries:

`paclog --commandline`

- Display only errors, warnings, and notes:

`paclog --warnings`

- Display package name and action type:

`paclog --package {{package_name}} --action {{install|upgrade|remove|...}}`

- Display the list of installed packages according to the log:

`paclog --pkglist`

- Display help:

`paclog --help`

- Display version:

`paclog --version`
