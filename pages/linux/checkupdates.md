# checkupdates

> Check pending updates in Arch Linux.
> More information: <https://manned.org/checkupdates>.

- Synchronize the database and list pending updates:

`checkupdates`

- List pending updates without syncing the database:

`checkupdates {{[-n|--nosync]}}`

- Display the list of pending updates if it differs from the last time this option was used:

`checkupdates {{[-c|--change]}}`

- List pending updates and download the packages to the `pacman` cache (`/var/cache/pacman/pkg`):

`checkupdates {{[-d|--download]}}`

- List pending updates using a specific `pacman` database:

`CHECKUPDATES_DB={{path/to/directory}} checkupdates`

- Display help:

`checkupdates {{[-h|--help]}}`
