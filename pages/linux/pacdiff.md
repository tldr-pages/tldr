# pacdiff

> Maintenance utility for `.pacorig`, `.pacnew` and `.pacsave` files created by `pacman`.
> More information: <https://man.archlinux.org/man/pacdiff>.

- Review files that need maintenance in interactive mode:

`pacdiff`

- Use sudo and sudoedit to remove and merge files:

`pacdiff --sudo`

- Store the original version of any file you `(O)verwrite with` as a `.bak`:

`pacdiff --sudo --backup`

- Override the program for `(M)erge`ing changes (`vim -d` is default):

`DIFFPROG={{editor}} pacdiff`

- Scan for configuration files with `locate` instead of using pacman database:

`pacdiff --locate`

- Display help:

`pacdiff --help`
