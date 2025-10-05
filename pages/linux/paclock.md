# paclock

> Lock/Unlock the libalpm database (used by pacman) to prevent or allow simultaneous package management operations.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclock.pod>.

- Lock the database (default behavior):

`paclock`

- Write the lock file path to stdout:

`paclock --print`

- Unlock the database:

`paclock --unlock`

- Lock the database(default):

`paclock --lock`

- Display help:

`paclock --help`

- Display version:

`paclock --version`
