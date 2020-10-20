# schroot

> Run command or interactive shell with special root directory. More customizable than standard chroot.

- Run command in a specific chroot:

`schroot -c {{chroot}} {{command}}`

- Pass options to a command in a specific chroot:

`schroot -c {{chroot}} {{command}} -- {{options for command}}

- Run command in all available chroots:

`schroot -a {{command}}`

- Specify user to use in a specific chroot:

`schroot -c {{chroot}} -u {{user}}`

- List available chroots:

`schroot -l`
