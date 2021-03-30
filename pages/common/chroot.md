# chroot

> Run command or interactive shell with special root directory.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Run command as new root directory:

`chroot {{path/to/new/root}} {{command}}`

- Specify user and group (ID or name) to use:

`chroot --userspec={{user:group}}`
