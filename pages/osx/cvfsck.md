# cvfsck

> Check and recover an Xsan volume.
> More information: <https://www.unix.com/man-page/osx/1/cvfsck>.

- Scan directories for name collisions that would occur on a case-insensitive filesystem:

`cvfsck -A`

- Provide a specific path to a configuration file to be used for overriding the implicit location:

`cvfsck -c {{path/to/configuration_file}}`

- Dump a significant amount of data to the standard output device (Internal debug use):

`cvfsck -d`

- Report statistics for extents in each file:

`cvfsck -e`

- Report free space fragmentation:

`cvfsck -f`
