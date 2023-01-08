# attrib

> Display or change attributes of files or directories.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Display all set attributes of files in the current directory:

`attrib`

- Display all set attributes of files in a specific directory:

`attrib {{path\to\directory}}`

- Display all set attributes of files and [d]irectories in the current directory:

`attrib /d`

- Display all set attributes of files in the current directory and [s]ub-directories:

`attrib /s`

- Add the `[r]ead-only` or `[a]rchive` or `[s]ystem` or `[h]idden` or `not content [i]ndexed` attribute to files or directories:

`attrib +{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`

- Remove a specific attribute of files or directories:

`attrib -{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`
