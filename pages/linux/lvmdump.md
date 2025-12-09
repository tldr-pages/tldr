# lvmdump

> Collect diagnostic information about LVM2 (Logical Volume Manager).
> By default, outputs a compressed tar archive with system and configuration data in the home directory.
> More information: <https://manned.org/lvmdump>.

- Generate a basic dump:

`lvmdump`

- Generate an extended dump with metadata and daemon info:

`lvmdump -a -l -m`

- Dump the information into a directory instead of a tarball:

`lvmdump -d {{path/to/directory}}`

- Display help:

`lvmdump -h`
