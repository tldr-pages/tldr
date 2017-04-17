# [mv](http://man7.org/linux/man-pages/man1/mv.1.html)
> Move or rename files and directories.

- Move files in arbitrary locations:

`mv {{source}} {{target}}`

- Do not prompt for confirmation before overwriting existing files:

`mv -f {{source}} {{target}}`

- Do not prompt for confirmation before overwriting existing files but write to standard error before overriding:

`mv -fi {{source}} {{target}}`

- Move files in verbose mode, showing files after they are moved:

`mv -v {{source}} {{target}}`
