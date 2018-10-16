# lrztar

> A wrapper for `lrzip` to simplify compression of directories.
> See also: `lrzuntar`, `lrunzip`.

- Archive a directory with tar, then compress:

`lrztar {{directory}}`

- Same as above, with ZPAQ - extreme compression, but very slow:

`lrztar -z {{directory}}`

- Specify output file name and/or path:

`lrztar -o {{outfilename}} {{directory}}`

- Override the number of processor threads to use:

`lrztar -p {{8}} {{directory}}`

- Force overwrite of existing files:

`lrztar -f {{directory}}`