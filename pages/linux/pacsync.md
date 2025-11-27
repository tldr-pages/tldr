# pacsync

> Update sync databases.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacsync.pod>.

- Update all sync databases:

`pacsync`

- Update specific sync databases:

`pacsync {{repository1 repository2 ...}}`

- Update sync databases even if they are already up-to-date:

`pacsync --force`

- Update sync databases using a specific configuration file:

`pacsync --config {{path/to/pacman.conf}}`

- Update sync databases and return true only if a database was actually updated:

`pacsync --updated`
