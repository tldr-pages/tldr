# chroot

> Run command or interactive shell with special root directory.
> More information: <https://www.gnu.org/software/coreutils/chroot>.

- Run command as new root directory:

`chroot {{path/to/new/root}} {{command}}`

- Use a specific user and group:

`chroot --userspec={{username_or_id:group_name_or_id}}`
