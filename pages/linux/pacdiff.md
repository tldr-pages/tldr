# pacdiff

> Pacorig, pacnew and pacsave maintenance utility for pacman.
> More information: <https://manned.org/pacdiff>.

- Look for files that need maintenance:

`pacdiff`

- Use sudoedit to merge or remove files:

`pacdiff --sudo`

- Store the original version of any file you `(O)verwrite with` as a `.bak`

`pacdiff --backup`

- Override the program for `(M)erge`ing changes (`vim -d` is default):

`DIFFPROG=meld pacdiff`

- Find files that need maintenance, apply changes with sudoedit, and keep backups:

`pacdiff -b -s`

- Scan for files with `locate` instead of searching pacmandb to find untracked files:

`pacdiff --locate`

- Display help:

`pacdiff --help`
