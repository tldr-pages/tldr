# systemd-sysusers

> Create system users and groups.
> If the config file is not specified, files in the `sysusers.d` directories are used.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-sysusers.html>.

- Create users and groups from a specific configuration file:

`systemd-sysusers {{path/to/file}}`

- Simulate processing configuration files, printing what would be done:

`systemd-sysusers --dry-run {{path/to/file}}`

- Print the contents of all configuration files (before each file, its name is printed as a comment):

`systemd-sysusers --cat-config`

- Create users based on files listed in the previous command:

`systemd-sysusers`
