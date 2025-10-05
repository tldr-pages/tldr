# pacconf

> queries and displays pacman's configuration options, showing either the full configuration or specific directive values as parsed by pacman.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacconf.pod>.

- List all available packages:

`pacconf`

- List configured repositories:

`pacconf --repo-list`

- Always show directive names even if only one directive is provided:

`pacconf --verbose`

- Display only first value of multi-value options:

`pacconf --single`

- Display help:

`pacconf --help`

- Display version:

`pacconf --version`
