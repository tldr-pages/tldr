# lrztar

> A wrapper for `lrzip` to simplify compression of directories.
> See also: `tar`, `lrzuntar`, `lrunzip`.

- Archive a directory with `tar`, then compress:

`lrztar {{path/to/directory}}`

- Same as above, with ZPAQ - extreme compression, but very slow:

`lrztar -z {{path/to/directory}}`

- Specify the output file:

`lrztar -o {{path/to/file}} {{path/to/directory}}`

- Override the number of processor threads to use:

`lrztar -p {{8}} {{path/to/directory}}`

- Force overwriting of existing files:

`lrztar -f {{path/to/directory}}`
