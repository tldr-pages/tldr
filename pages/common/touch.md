# touch

> Create files and set access/modification times.
> More information: <https://manned.org/man/freebsd-13.1/touch>.

- Create specific files:

`touch {{path/to/file1 path/to/file2 ...}}`

- Set the file [a]ccess or [m]odification times to the current one and don't [c]reate file if it doesn't exist:

`touch -c -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- Set the file [t]ime to a specific value and don't [c]reate file if it doesn't exist:

`touch -c -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- update the files' timestamp to the [r]ef_file's timestamp, and don't [c]reate file if not exist:

`touch -c -r {{path/to/ref_file}} {{path/to/file1 path/to/file2 ...}}`
