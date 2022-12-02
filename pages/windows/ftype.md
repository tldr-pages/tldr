# ftype

> Display or modify file types used for file extension association.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftype>.

- Display a list of all file types:

`ftype`

- Display the associated program for a specific file type:

`ftype {{path/to/file}}`

- Set the associated program for a specific file type:

`ftype {{path/to/file}}="{{path/to/executable_command}}"`
