# fc

> Compare the differences between two files or sets of files.
> Use wildcards (*) to compare sets of files.

- Compare 2 specified files:

`fc {{path/to/file_1}} {{path/to/file_2}}`

- Perform a case-insensitive comparison:

`fc /c {{path/to/file_1}} {{path/to/file_2}}`

- Compare files as Unicode text:

`fc /u {{path/to/file_1}} {{path/to/file_2}}`

- Compare files as ASCII text:

`fc /l {{path/to/file_1}} {{path/to/file_2}}`

- Compare files as binary:

`fc /b {{path/to/file_1}} {{path/to/file_2}}`

- Disable tab-to-space expansion:

`fc /t {{path/to/file_1}} {{path/to/file_2}}`

- Compress whitespace (tabs and spaces) for comparisons:

`fc /w {{path/to/file_1}} {{path/to/file_2}}`
