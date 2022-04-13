# touch

> Creates files and sets access/modification time.
> More information: <https://www.gnu.org/software/coreutils/touch>.

- Create specific files:

`touch {{path/to/file{1,2,...} }}`

- Update file access/modification time to the current one:

`touch --time={{access|modify}} {{path/to/file{1,2,...} }}`

- Update file access/modification [t]ime to a specific one:

`touch --time={{access|modify}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file{1,2,...} }}`

- Update file access/modification time to a specific file time (`--reference` argument):

`touch --time={{access|modify}} --reference={{path/to/file}} {{path/to/file{1,2,...} }}`
