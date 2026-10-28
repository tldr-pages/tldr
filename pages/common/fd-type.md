# fd --type

> Search for specific filetypes.
> More information: <https://manned.org/fd>.

- Search for regular files:

`fd {{[-t|--type]}} {{[f|file]}}`

- Search for directories:

`fd {{[-t|--type]}} {{[d|directory]}}`

- Search for files with the executable bit set:

`fd {{[-t|--type]}} {{[x|executable]}}`

- Search for empty files and directories:

`fd {{[-t|--type]}} {{[e|empty]}}`

- Search for symbolic links:

`fd {{[-t|--type]}} {{[l|symlink]}}`

- Search for block devices:

`fd {{[-t|--type]}} {{[b|block-device]}}`

- Search for regular files that are also empty:

`fd {{[-t|--type]}} {{[f|file]}} {{[-t|--type]}} {{[e|empty]}}`
