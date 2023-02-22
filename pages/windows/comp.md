# comp

> Compare the contents of two files or sets of files.
> Use wildcards (*) to compare sets of files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Compare files interactively:

`comp`

- Compare two specified files:

`comp {{path\to\file1}} {{path\to\file2}}`

- Compare two sets of files:

`comp {{path\to\directory1}}\* {{path\to\directory2}}\*`

- Display differences in decimal format:

`comp /d {{path\to\file1}} {{path\to\file2}}`

- Display differences in ASCII format:

`comp /a {{path\to\file1}} {{path\to\file2}}`

- Display line numbers for differences:

`comp /l {{path\to\file1}} {{path\to\file2}}`

- Compare files case-insensitively:

`comp /c {{path\to\file1}} {{path\to\file2}}`

- Compare only the first 5 lines of each file:

`comp /n={{5}} {{path\to\file1}} {{path\to\file2}}`
