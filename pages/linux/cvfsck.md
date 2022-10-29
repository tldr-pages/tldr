# cvfsk

> Check and Recover a Xsan Volume.
> More information: <https://www.unix.com/man-page/osx/1/cvfsck/>.

- Scan directories for name collisions that would occur on a case-insensitive filesystem:

`cvfsk -A`

- Provide a specific path to a configuration file that is to be used, overriding the implicit location:

`cvfsk -c {{pathname}}`

- Internal debug use to dump a significant amount of data to the standard output device:

`cvfsk -d`

- Report statistics for extents in each file:

`cvfsk -e`

- Report free space fragmentation:

`cvfsk -f`
