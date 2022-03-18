# comp

> Compare the contents of two files or sets of files. Wildcards are supported.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/comp>.

- Compare files interactively:

`comp`

- Compare the specified files:

`comp {{path/to/file1}} {{path/to/file2}}`

- Print the differences in [d]ecimal format:

`comp /d {{path/to/file1}} {{path/to/file2}}`

- Print the differences in ASCII format:

`comp /a {{path/to/file1}} {{path/to/file2}}`

- Print the [l]ine numbers for differences:

`comp /l {{path/to/file1}} {{path/to/file2}}`

- Compare the specified files [c]ase-insensitively:

`comp /c {{path/to/file1}} {{path/to/file2}}`

- Compare the first 5 lines of each file:

`comp /n={{5}} {{path/to/file1}} {{path/to/file2}}`
