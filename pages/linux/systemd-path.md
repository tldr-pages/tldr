# systemd-path

> List and query system and user paths.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-path.html>.

- When invoked without arguments, the command displays a list of known paths and their current values:

`systemd-path`

- When at least one argument is provided, the path with the specified name is queried, and its value is displayed:

`systemd-path "{{query_name}}"`

- Print paths with the specified string as a suffix:

`systemd-path --suffix="{{suffix_string}}"`

- Print a short version string and then exit:

`systemd-path --version`
