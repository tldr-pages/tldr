# pacdiff

> Pacorig, pacnew and pacsave maintenance utility for pacman.
> More information: <https://man.archlinux.org/man/pacdiff>.

- Look for files that need maintenance:

`pacdiff`

- Use sudo and sudoedit to remove and merge files:

`pacdiff --sudo`

- Store the original version of any file you `(O)verwrite with` as a `.bak`:

`pacdiff -s --backup`

- Override the program for `(M)erge`ing changes (`vim -d` is default):

`DIFFPROG={{meld}} pacdiff`

- Scan for files with `locate` instead of searching pacmandb to find untracked files:

`pacdiff --locate`

- Display help:

`pacdiff --help`
