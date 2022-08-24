# touch

> Create files and set access/modification times.
> More information: <https://www.gnu.org/software/coreutils/touch>.

- Create specific files:

`touch {{path/to/file1 path/to/file2 ...}}`

- Set the file access/modification times to the current one:

`touch --no-create --time={{access|modify}} {{path/to/file1 path/to/file2 ...}}`

- Set the file [t]ime to a specific value:

`touch --no-create --time={{access}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Set the file time of a specific file to the time of another file:

`touch --no-create --time={{access}} --reference={{~/.emacs}} {{path/to/file1 path/to/file2 ...}}`
