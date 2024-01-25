# systemd-sysusers

> Create system users and groups.
> If the config file is not specified, files in the `sysusers.d` directories are used.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-sysusers.html>.

- Create users and groups from a specific configuration file:

`systemd-sysusers {{path/to/file}}`

- Process configuration files and print what would be done without actually doing anything:

`systemd-sysusers --dry-run {{path/to/file}}`

- Print the contents of all configuration files (before each file, its name is printed as a comment):

`systemd-sysusers --cat-config`
