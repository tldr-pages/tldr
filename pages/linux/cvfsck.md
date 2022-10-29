# cvfsck

> Check and Recover a Xsan Volume.
> More information: <https://www.unix.com/man-page/osx/1/cvfsck/>.

- Scan directories for name collisions that would occur on a case-insensitive filesystem:

`cvfsck -A`

- Provide a specific path to a configuration file that is to be used, overriding the implicit location:

`cvfsck -c {{path/to/configuration_file}}`

- Internal debug use to dump a significant amount of data to the standard output device:

`cvfsck -d`

- Report statistics for extents in each file:

`cvfsck -e`

- Report free space fragmentation:

`cvfsck -f`
