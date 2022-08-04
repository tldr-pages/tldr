# touch

> Create files and set access/modification time.
> More information: <https://www.gnu.org/software/coreutils/touch>.

- Create specific files:

`touch {{path/to/file1 path/to/file2 ...}}`

- Update file access/modification time to the current one:

`touch --no-create --time={{access|modify}} {{path/to/file1 path/to/file2 ...}}`

- Update file [t]ime to a specific one:

`touch --no-create --time={{mode}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Update file time to a specific file time:

`touch --no-create --time={{mode}} --reference={{path/to/file}} {{path/to/file1 path/to/file2 ...}}`
