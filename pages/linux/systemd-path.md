# systemd-path

> List and query system and user paths.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-path.html>.

- Display a list of known paths and their current values:

`systemd-path`

- Query the specified path and display its value:

`systemd-path "{{path_name}}"`

- Suffix printed paths with `suffix_string`:

`systemd-path --suffix {{suffix_string}}`

- Print a short version string and then exit:

`systemd-path --version`
