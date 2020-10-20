# schroot

> Run command or interactive shell with special root directory. More customizable than standard chroot.
> Source code: https://gitlab.com/codelibre/schroot.
> More information: <https://wiki.debian.org/Schroot>.

- Run command in a specific chroot:

`schroot --chroot {{chroot}} {{command}}`

- Pass options to a command in a specific chroot:

`schroot --chroot {{chroot}} {{command}} -- {{options for command}}`

- Run command in all available chroots:

`schroot --all {{command}}`

- Specify user to use in a specific chroot:

`schroot --chroot {{chroot}} --user {{user}}`

- List available chroots:

`schroot --list`
