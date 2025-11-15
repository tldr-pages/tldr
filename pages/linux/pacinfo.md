# pacinfo

> Display information about installed packages.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacinfo.pod>.

- Display information about a specific package:

`pacinfo {{package_name}}`

- Disable low-speed timeouts for downloads:

`pacinfo --no-timeout {{package_name}}`

- Display sizes in bytes and date values as Unix timestamps:

`pacinfo --raw {{package_name}}`

- Display additional package information:

`pacinfo --verbose {{package_name}}`

- Display help:

`pacinfo --help`

- Display version:

`pacinfo --version`
