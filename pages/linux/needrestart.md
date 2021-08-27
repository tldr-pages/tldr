# needrestart

> Checks which daemons need to be restarted after library upgrades.
> More information: <https://github.com/liske/needrestart>.

- List outdated process:

`needrestart`

- Interactively restart services:

`sudo needrestart`

- Run in [v]erbose or [q]uiet mode:

`needrestart -{{v|q}}`

- Check for obsoleteneed kernel:

`needrestart -k`

- Check for obsolete CPU microcode:

`needrestart -w`

- Display output in batch mode:

`needrestart -b`

- Run using a configuration file:

`needrestart -c {{path/to/config}}`

- Display help:

`needrestart --help`
