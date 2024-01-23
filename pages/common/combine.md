# combine

> Perform set operations on lines of two files.
> The order of the output lines is determined by the order of the lines in the first file.
> See also: `diff`.
> More information: <https://joeyh.name/code/moreutils/>.

- Output lines that are in both specified files:

`combine {{path/to/file1}} and {{path/to/file2}}`

- Output lines that are in the first but not in the second file:

`combine {{path/to/file1}} not {{path/to/file2}}`

- Output lines that in are in either of the specified files:

`combine {{path/to/file1}} or {{path/to/file2}}`

- Output lines that are in exactly one of the specified files:

`combine {{path/to/file1}} xor {{path/to/file2}}`
