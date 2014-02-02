# mv

> Move or rename files and directories

- Move files in abitrary locations

`mv {{path/to/source}} {{path/to/target}}`

- Move a file to a parent directory

`mv {{/path/to/source}} ../{{/path/to/target}}`

- Do not promt for confirmation before overwriting existing files

`mv -f {{path/to/source}} {{path/to/target}}`

- Do not promt for confirmation before overwriting existing files but write to standard error before overriding

`mv -fi {{path/to/source}} {{path/to/target}}`

- Move files in verbose mode, showing files after they are moved

`mv -v {{path/to/source}} {{path/to/target}}`
