# paclock

> Lock/unlock the libalpm database (used by `pacman`) to prevent or allow simultaneous package management operations.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclock.pod>.

- Lock the database:

`paclock`

- Write the lock file path to `stdout` (without locking the database):

`paclock --print`

- Unlock the database:

`paclock --unlock`

- Display help:

`paclock --help`

- Display version:

`paclock --version`
