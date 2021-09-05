# needrestart

> Check which daemons need to be restarted after library upgrades.
> More information: <https://github.com/liske/needrestart>.

- List outdated processes:

`needrestart`

- Interactively restart services:

`sudo needrestart`

- List outdated processes in [v]erbose or [q]uiet mode:

`needrestart -{{v|q}}`

- Check if the kernel is obsolete:

`needrestart -k`

- Check if the CPU microcode is obsolete:

`needrestart -w`

- List outdated processes in [b]atch mode:

`needrestart -b`

- List outdated processed using a specific configuration file:

`needrestart -c {{path/to/config}}`

- Display help:

`needrestart --help`
