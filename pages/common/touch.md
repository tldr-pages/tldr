# touch

> Create files and set access/modification times.
> More information: <https://manned.org/touch>.

- Create specific files:

`touch {{path/to/file1 path/to/file2 ...}}`

- Set the file [a]ccess or [m]odification times to the current one and don't create file if it doesn't exist:

`touch {{[-c|--no-create]}} -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- Set the file [t]ime to a specific value and don't create file if it doesn't exist:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Set the files' timestamp to the reference file's timestamp, and do not create the file if it does not exist:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{path/to/reference_file}} {{path/to/file1 path/to/file2 ...}}`
