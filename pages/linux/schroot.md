# schroot

> Run command or start an interactive shell with a special root directory. More customizable than standard chroot.
> More information: <https://wiki.debian.org/Schroot>.

- Run command in a specific chroot:

`schroot --chroot {{chroot}} {{command}}`

- Run a command with options in a specific chroot:

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- Run command in all available chroots:

`schroot --all {{command}}`

- Start an interactive shell with in a specific chroot as a specific user:

`schroot --chroot {{chroot}} --user {{user}}`

- List available chroots:

`schroot --list`
