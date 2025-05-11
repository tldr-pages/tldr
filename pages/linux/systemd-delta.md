# systemd-delta

> Find overridden systemd-related configuration files.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-delta.html>.

- Show all overridden configuration files:

`systemd-delta`

- Show only files of specific types (comma-separated list):

`systemd-delta {{[-t|--type]}} {{masked|equivalent|redirected|overridden|extended|unchanged}}`

- Show only files whose path starts with the specified prefix (Note: A prefix is a directory containing subdirectories with systemd configuration files):

`systemd-delta {{/etc|/run|/usr/lib|...}}`

- Further restrict the search path by adding a suffix (the prefix is optional):

`systemd-delta {{prefix}}/{{tmpfiles.d|sysctl.d|systemd/system|...}}`
