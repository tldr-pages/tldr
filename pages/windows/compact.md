# compact

> Display or change the compression state of files and directories on NTFS partitions.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/compact>.

- Display the compression status of files in the current directory:

`compact`

- Compress a specific file:

`compact /c {{path\to\file}}`

- Uncompress a specific file:

`compact /u {{path\to\file}}`

- Compress all files in a directory and its subdirectories:

`compact /c /s {{path\to\directory}}`

- Uncompress all files in a directory and its subdirectories:

`compact /u /s {{path\to\directory}}`
