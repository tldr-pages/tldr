# replace

> Replaces files. It is related to robocopy, move, copy, and del. More information: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/replace.

- Replace the destination file with the one from the source directory:

`replace {{path/to/file_or_directory}} {{path/to/destination}}`

- Only adds files that do not already exist:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /a`

- Prompt before it replaces each file:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /p`

- Replace even read only files:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /r`

- Wait for you to insert a disk before it replaces files (originally to allow inserting a floppy disk):

`replace {{path/to/file_or_directory}} {{path/to/destination}} /w`

- Replaces all files in subfolders of the destination:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /s`

- Only replaces files in the destination directory which are older than the files in the source directory:

`replace {{path/to/file_or_directory}} {{path/to/destination}} /u`

- Display detailed usage information:

`replace /?`
