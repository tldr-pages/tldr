# fc

> Compare the differences between two files or sets of files.
> Use wildcards (*) to compare sets of files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- Compare 2 specified files:

`fc {{path\to\file1}} {{path\to\file2}}`

- Perform a case-insensitive comparison:

`fc /c {{path\to\file1}} {{path\to\file2}}`

- Compare files as Unicode text:

`fc /u {{path\to\file1}} {{path\to\file2}}`

- Compare files as ASCII text:

`fc /l {{path\to\file1}} {{path\to\file2}}`

- Compare files as binary:

`fc /b {{path\to\file1}} {{path\to\file2}}`

- Disable tab-to-space expansion:

`fc /t {{path\to\file1}} {{path\to\file2}}`

- Compress whitespace (tabs and spaces) for comparisons:

`fc /w {{path\to\file1}} {{path\to\file2}}`
