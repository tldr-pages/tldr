# systemd-sysusers

> creates system users and groups.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-sysusers.html>.

- Create Users and Groups from a Specific Configuration File:

`systemd-sysusers {{config_pathpath}}`

- Simulate processing a configuration file without creating users and groups to preview the entries that would be generated:

`systemd-sysusers --dry-run {{config_pathpath}}`

- Print the contents of the specified configuration file:

`systemd-sysusers --cat-config {{config_path}}`

