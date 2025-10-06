# pacini

> Query pacman-style configuration files.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacini.pod>.

- Show the full parsed configuration file (default: `stdin`):

`pacini {{path/to/file}}`

- List configured sections:

`pacini --section-list`

- Always show directive names even if only one directive is provided:

`pacini --verbose {{directive}}`

- Display directives listed in a specific section:

`pacini --section {{section_name}}`

- Display help:

`pacini --help`

- Display version:

`pacini --version`
