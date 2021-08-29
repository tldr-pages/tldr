# needrestart

> Checks which daemons need to be restarted after library upgrades.
> More information: <https://github.com/liske/needrestart>.

- List outdated process:

`needrestart`

- Interactively restart services:

`sudo needrestart`

- Run in [v]erbose or [q]uiet mode:

`needrestart -{{v|q}}`

- Check if the kernel is obsolete:

`needrestart -k`

- Check if CPU microcode is obsolete:

`needrestart -w`

- Display output in batch mode:

`needrestart -b`

- Run using a configuration file:

`needrestart -c {{path/to/config}}`

- Display help:

`needrestart --help`
