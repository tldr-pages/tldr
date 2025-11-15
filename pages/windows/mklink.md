# mklink

> Create symbolic links.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- Create a symbolic link to a file:

`mklink {{path\to\link_file}} {{path\to\source_file}}`

- Create a symbolic link to a directory:

`mklink /d {{path\to\link_file}} {{path\to\source_directory}}`

- Create a hard link to a file:

`mklink /h {{path\to\link_file}} {{path\to\source_file}}`

- Create a directory junction:

`mklink /j {{path\to\link_file}} {{path\to\source_file}}`
