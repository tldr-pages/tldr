# touch

> Create files and set access/modification time.
> More information: <https://manned.org/man/freebsd-13.0/touch>.

- Create specific files:

`touch {{path/to/file1 path/to/file2 ...}}`

- Update file [a]ccess/[m]odification time to the current one:

`touch -c -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- Update file [t]ime to a specific one:

`touch -c -{{a|m}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Update file time to a specific file time:

`touch -c -{{a|m}} -r {{path/to/file}} {{path/to/file1 path/to/file2 ...}}`
