# pacini

> Query pacman-style configuration files.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacini.pod>.

- Show the full parsed configuration file (default: `/etc/pacman.conf`):

`pacini`

- List configured sections:

`pacini --section-list`

- Display directive names:

`pacini --verbose`

- Display directives listed in a specific section:

`pacini --section {{section_name}}`

- Query a custom configuration file:

`pacini {{path/to/config.conf}}`

- Display help:

`pacini --help`

- Display version:

`pacini --version`
