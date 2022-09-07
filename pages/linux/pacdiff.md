# pacdiff

> Pacorig, pacnew and pacsave maintenance utility for pacman.
> If you want to use a different program for diffs, set the `DIFFPROG` enviromental variable to point to your desired binary, with any needed flags. `vim -d` is the default.
> More information: <https://man.archlinux.org/man/pacdiff.8>.

- Look for files that need maintenance:

`pacdiff`

- Use sudoedit to merge or remove files:

`pacdiff -s`

- Save old versions of modified files as `.bak` files:

`pacdiff -b`

- Find files that need maintenance, apply changes with sudoedit, and keep backups:

`pacdiff -b -s`

- Scan for files with `locate` instead of using pacmandb (much slower, but finds files missing from db):

`pacdiff -l`

- Display help:

`pacdiff -h`
