# mountpoint

> Test if a directory is a filesystem mountpoint.
> More information: <https://manned.org/mountpoint>.

- Check if a directory is a mountpoint:

`mountpoint {{path/to/directory}}`

- Check if a directory is a mountpoint without showing any output:

`mountpoint {{[-q|--quiet]}} {{path/to/directory}}`

- Show major/minor numbers of a mountpoint's filesystem:

`mountpoint {{[-d|--fs-devno]}} {{path/to/directory}}`
