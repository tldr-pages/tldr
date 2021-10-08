# sdiff

> Compare the differences between and optionally merge 2 files.
> More information: <https://manned.org/sdiff>.

- Compare 2 files:

`sdiff {{path/to/file1}} {{path/to/file2}}`

- Compare 2 files, ignoring all tabs and whitespace:

`sdiff -W {{path/to/file1}} {{path/to/file2}}`

- Compare 2 files, ignoring whitespace at the end of lines:

`sdiff -Z {{path/to/file1}} {{path/to/file2}}`

- Compare 2 files in a case-insensitive manner:

`sdiff -i {{path/to/file1}} {{path/to/file2}}`

- Compare and then merge, writing the output to a new file:

`sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`
